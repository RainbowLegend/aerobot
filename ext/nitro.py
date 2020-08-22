from discord.ext import commands


class NitroPerks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild = bot.get_guild(288455332173316106)

    @commands.command(name="customrole")
    @commands.has_any_role(702614991446081578)
    async def roles(self, ctx, action, *, args):
        if action == "create":
            newrole = await self.guild.create_role(name=ctx.author.id, reason=f"Nitro Booster Role for {ctx.author.id}")
            ghost = self.guild.get_roles(702605281204502638)
            current_guild_roles = self.guild.roles()
            await newrole.edit(position=current_guild_roles.index(ghost) + 1)
            await ctx.send("Your new role has been created!")


def setup(bot):
    bot.add_cog(NitroPerks(bot))
