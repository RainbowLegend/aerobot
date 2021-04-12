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
            user = await self.bot.wait_for('message', check=lambda
                m: m.author.id == ctx.author.id and isinstance(m.channel, discord.DMChannel), timeout=300)
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
            reason = await self.bot.wait_for('message', check=lambda
                m: m.author.id == ctx.author.id and isinstance(m.channel, discord.DMChannel), timeout=300)
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

    @commands.command(name="suggest")
    async def suggest(self, ctx):
        guild = self.bot.get_guild(702600628601356359)
        channel = guild.get_channel(831277854528110642)
        emb = discord.Embed(color=discord.Color.blurple())
        emb.add_field(name="Apply to host a gamenight",
                      value="If at any time you wish to cancel the form, type `cancel`.\n"
                            "All questions will time out after 5 minutes.")
        timeout = discord.Embed(color=discord.Color.red(), description="Report form timed out.")
        cancel = discord.Embed(color=discord.Color.red(), description="Report form cancelled.")

        await ctx.author.send(embed=emb)
        await ctx.author.send("When do you want to host the gamenight? Please include the timezone.")
        try:
            timezone = await ctx.bot.wait_for('message', check=lambda
                m: m.author.id == ctx.author.id and isinstance(m.channel, discord.DMChannel), timeout=300).content
            if timezone.lower().strip() == "cancel":
                return await ctx.author.send(embed=cancel)

            await ctx.author.send("What game are you planning to host?")
            game = await ctx.bot.wait_for('message', check=lambda
                m: m.author.id == ctx.author.id and isinstance(m.channel, discord.DMChannel), timeout=300).content
            if game.lower().strip() == "cancel":
                return await ctx.author.send(embed=cancel)

            await ctx.author.send("How long are you planning to host?")
            duration = await ctx.bot.wait_for('message', check=lambda
                m: m.author.id == ctx.author.id and isinstance(m.channel, discord.DMChannel), timeout=300).content
            if duration.lower().strip() == "cancel":
                return await ctx.author.send(embed=cancel)

        except asyncio.TimeoutError:
            return await ctx.author.send(embed=timeout)

        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name="When the gamenight will be hosted", value=timezone)
        embed.add_field(name="Game to be hosted", value=game)
        embed.add_field(name="Duration of gamenight", value=duration)
        await ctx.author.send("Thank you for applying to host! Here is a copy of your application.", embed=embed)
        embed.add_field(name="Applicant", value=ctx.author.mention)
        await channel.send("A new application has been filed.", embed=embed)


def setup(bot):
    bot.add_cog(UserForms(bot))
