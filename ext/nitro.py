import discord
import asyncio
from discord.ext import commands


class NitroPerks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def customrole(self, ctx):
      pass

    @customrole.command(name="create")
    async def create(self, ctx):
        self.guild = self.bot.get_guild(702600628601356359)

        if discord.utils.get(self.guild.roles, name=str(ctx.author.id)):
            return await ctx.send("You already have a custom role!")

        ghostRole = self.guild.get_role(702605281204502638)

        newrole = await self.guild.create_role(name=ctx.author.id, reason=f"Nitro Booster Role for {ctx.author.id}")
        await asyncio.sleep(1)
        await newrole.edit(position=self.guild.roles.index(ghostRole))
        await asyncio.sleep(1)
        await ctx.author.add_roles(newrole, reason="Nitro Booster Role")
        return await ctx.send("Your new role has been created!")

    @customrole.command(name="color")
    async def color(self, ctx, *, hexinput=None):

        if discord.utils.get(self.guild.roles, name=str(ctx.author.id)) is None:
            return await ctx.send("Create a role before using this command!")

        userrole = discord.utils.get(self.guild.roles, name=str(ctx.author.id))

        try:
            await userrole.edit(color=discord.Color(value=int(hexinput.strip("#"), 16)))
            return await ctx.send(f"You have changed your role's color to {hexinput}!")
        except ValueError:
            return await ctx.send("Input a valid hex code such as `#FFFFFF`!")

def setup(bot):
    bot.add_cog(NitroPerks(bot))
