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
    async def on_ready(self):
        self.guild = self.bot.get_guild(702600628601356359)

    @customrole.command(name="create")
    async def create(self, ctx):
        if discord.utils.get(self.guild.roles, name=str(ctx.author.id)):
            return await ctx.send("You already have a custom role!")

        ghost_role = self.guild.get_role(702605281204502638)

        newrole = await self.guild.create_role(name=ctx.author.id, reason=f"Nitro Booster Role for {ctx.author.id}")
        await asyncio.sleep(1)
        await newrole.edit(position=self.guild.roles.index(ghost_role))
        await asyncio.sleep(1)
        await ctx.author.add_roles(newrole, reason="Nitro Booster Role")
        with open("nitro.json") as f:
            db = json.load(f)
            db[str(ctx.author.id)] = newrole.id
            json.dump(db, f)
        return await ctx.send("Your new role has been created!")

    @customrole.command(name="color")
    async def color(self, ctx, *, hexinput=None):
        with open("nitro.json") as f:
            db = json.load(f)
        if not discord.utils.get(self.guild.roles, name=str(ctx.author.id)) or str(ctx.author.id) not in db.keys():
            return await ctx.send("Create a role before using this command!")

        user_role = discord.utils.get(self.guild.roles, name=str(ctx.author.id)) \
                    or self.guild.get_role(db[str(ctx.author.id)])

        if str(ctx.author.id) not in db.keys():
            db[str(ctx.author.id)] = user_role.id

        try:
            await user_role.edit(color=discord.Color(value=int(hexinput.strip("#"), 16)))
            return await ctx.send(f"You have changed your role's color to {hexinput}!")
        except ValueError:
            return await ctx.send("Input a valid hex code such as `#FFFFFF`!")

    @customrole.command(name="name")
    async def name(self, ctx, *, name):
        with open("ntiro.json") as f:
            db = json.load(f)
        if not discord.utils.get(self.guild.roles, name=str(ctx.author.id)) or str(ctx.author.id) not in db.keys():
            return await ctx.send("Create a role before using this command!")

        user_role = discord.utils.get(self.guild.roles, name=str(ctx.author.id)) \
                    or self.guild.get_role(db[str(ctx.author.id)])

        if str(ctx.author.id) not in db.keys():
            db[str(ctx.author.id)] = user_role.id

        await user_role.edit(name=name)
        return await ctx.send(f"Your role's name has been changed to **{name}**")


def setup(bot):
    bot.add_cog(NitroPerks(bot))
