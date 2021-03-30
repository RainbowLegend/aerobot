import asyncio
import discord
from discord.ext import commands


class UserForms(commands.Cog):
    """Report and Hosting Forms"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="report")
    async def report(self, ctx):
        guild = self.bot.get_guild(702600628601356359)
        channel = guild.get_channel(826497907116998676)
        emb = discord.Embed(color=discord.Color.blurple())
        emb.add_field(name="Report a user for breaking a rule",
                      value="If at any time you wish to cancel the form, type `cancel`.\n"
                            "All questions will time out after 5 minutes.")

        timeout = discord.Embed(color=discord.Color.red(), description="Report form timed out.")
        cancel = discord.Embed(color=discord.Color.red(), description="Report form cancelled.")
        await ctx.author.send(embed=emb)
        await ctx.author.send(
            "Who are you reporting? Please include either their user ID or full username (i.e. `MystLegend#2265` or "
            "`222147236728012800`). "
        )
        try:
            user = await self.bot.wait_for('message', check=lambda m: m.author.id == ctx.author.id, timeout=300)
            if user.content.lower() == "cancel":
                return await ctx.author.send(embed=cancel)
            try:
                ctx.guild = guild
                ctx.channel = channel
                user = await commands.UserConverter().convert(ctx, user.content)
            except commands.BadArgument:
                user = user
        except asyncio.TimeoutError:
            return await ctx.author.send(embed=timeout)

        await ctx.author.send(
            "Please describe what happened and what rule(s) was broken. Please add as much detail as possible as this "
            "will help us to resolve any issues quickly.")
        try:
            reason = await self.bot.wait_for('message', check=lambda m: m.author.id == ctx.author.id, timeout=300)
        except asyncio.TimeoutError:
            return await ctx.author.send(embed=timeout)

        await ctx.author.send("Thank you for your report!")
        report = discord.Embed(color=discord.Color.blurple())
        report.add_field(name="Reported by", value=ctx.author.mention)
        if isinstance(user, discord.User) or isinstance(user, discord.Member):
            report.add_field(name="Offending member", value=user.mention)
        else:
            report.add_field(name="Offending member", value=user.content)
        report.add_field(name="Report description", value=reason.content)
        await channel.send(embed=report)


def setup(bot):
    bot.add_cog(UserForms(bot))
