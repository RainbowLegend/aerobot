import discord
import asyncio
import json
from discord.ext import commands


class NitroPerks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def customrole(self, ctx):
        pass

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(702600628601356359)
        if before.guild.id != 702600628601356359:
            return
        nitro_booster = guild.get_role(702614991446081578)
        if nitro_booster in before.roles and nitro_booster not in after.roles:
            with open("nitro.json") as f:
                db = json.load(f)
            user_role = guild.get_role(db[str(after.id)])
            await after.remove_roles(user_role, reason="nitro boost removal")
            await user_role.delete(reason="nitro boost removal")
            del db[str(after.id)]
            await after.send("Your custom role has been removed because you are no longer nitro boosting the server.")
            with open("nitro.json", "w") as f:
                json.dump(db, f, indent=2)

    @customrole.command(name="create")
    async def create(self, ctx):
        guild = self.bot.get_guild(702600628601356359)
        with open("nitro.json") as f:
            db = json.load(f)
        if str(ctx.author.id) in db.keys():
            return await ctx.send("You already have a custom role!")
        ghost_role = guild.get_role(702605281204502638)
        if (guild.get_role(702614991446081578) not in ctx.author.roles) and \
                (guild.get_role(702601007368241173) not in ctx.author.roles):
            return await ctx.send("You need to be nitro boosting to get a custom role!")
        with open("nitro.json") as f:
            db = json.load(f)
        newrole = await guild.create_role(name=ctx.author.id, reason=f"Nitro Booster Role for {ctx.author.id}")
        await asyncio.sleep(1)
        await newrole.edit(position=guild.roles.index(ghost_role))
        await asyncio.sleep(1)
        await ctx.author.add_roles(newrole, reason="Nitro Booster Role")
        with open("nitro.json", "w") as f:
            db[str(ctx.author.id)] = newrole.id
            json.dump(db, f, indent=2)
        return await ctx.send("Your new role has been created!")

    @customrole.command(name="color")
    async def color(self, ctx, *, hexinput=None):
        guild = self.bot.get_guild(702600628601356359)
        with open("nitro.json") as f:
            db = json.load(f)
        if str(ctx.author.id) not in db.keys():
            return await ctx.send("Create a role before using this command!")

        user_role = guild.get_role(db[str(ctx.author.id)])

        try:
            await user_role.edit(color=discord.Color(value=int(hexinput.strip("#"), 16)))
            return await ctx.send(f"You have changed your role's color to {hexinput}!")
        except ValueError:
            return await ctx.send("Input a valid hex code such as `#FFFFFF`!")

    @customrole.command(name="name")
    async def name(self, ctx, *, name):
        guild = self.bot.get_guild(702600628601356359)
        with open("nitro.json") as f:
            db = json.load(f)
        if str(ctx.author.id) not in db.keys():
            return await ctx.send("Create a role before using this command!")

        user_role = guild.get_role(db[str(ctx.author.id)])

        await user_role.edit(name=name)
        return await ctx.send(f"Your role's name has been changed to **{name}**")


def setup(bot):
    bot.add_cog(NitroPerks(bot))
