import discord
from discord.ext import commands


class AnticipationNotifications:
    """Notifications for the Anticipation gamemode."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def anticipation(self, ctx: commands.Context):
        """Toggle for the Anticipation notifications."""
        role = ctx.guild.get_role(529447810127495168)

        if role.id not in (r.id for r in ctx.author.roles):
            await ctx.author.add_roles(role, reason="/anticipation")
            embed = discord.Embed(
                colour=discord.Colour.green(),
                description="Anticipation Notifications successfully added."
            )
            await ctx.send(embed=embed)

        else:
            await ctx.author.remove_roles(role, reason="/anticipation")
            embed = discord.Embed(
                colour=discord.Colour.red(),
                description="Anticipation Notifications successfully removed."
            )
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    c = AnticipationNotifications(bot)
    bot.add_cog(c)
