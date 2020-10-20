import discord
import asyncio
import json
from discord.ext import commands
from datetime import datetime, timedelta
# from aioscheduler import TimedScheduler


class RegularAssigner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.scheduler = TimedScheduler()
        # self.scheduler.start()

    @staticmethod
    def activity_check(messages: list, time_sep: int) -> int:
        messages = [x for x in messages if x.channel.id not in [702603189324873768, 748238536636891217]]
        message_total = 0
        last_time = datetime.now()
        for message in messages:
            if abs((message.created_at - last_time).seconds) > (time_sep * 60):
                last_time = message.created_at
                message_total += 1
        return message_total

    async def update_regulars(self, scheduled=True):
        guild = self.bot.get_guild(702600628601356359)

        now = datetime.now()
        week_ago = datetime.utcnow() - timedelta(days=7)
        channels = [702601830013599814, 702602469812863106, 717090761056976948, 702602837737078897, 702603094189670483,
                    702600628601356362, 702603144693022751, 702603364575346769, 702603823620816946]
        # tos-general, gamenights, ranked-lounge, tos-matches, trial-reports, general, flummery, pets, art
        server_history = []
        for channel in channels:
            channel_history = await (guild.get_channel(channel)).history(after=week_ago, limit=None).flatten()
            server_history = server_history + channel_history
        for member in guild.members:
            total_messages = self.activity_check(server_history, 3)
            if total_messages >= 55:
                role = guild.get_role(766771845247795280)
                if role not in member.roles:
                    await member.add_roles(role, reason="Added regular role")
        if scheduled:
            now = datetime.utcnow()
            next_monday = now + timedelta(days=(7 - now.weekday()))
            # self.scheduler.schedule(self.update_regulars(), next_monday)

    @commands.command()
    async def mr(self, ctx):
        await self.update_regulars(scheduled=False)
        await ctx.send("Roles given")

    """
    @commands.Cog.listener()
    async def on_ready(self):
        now = datetime.utcnow()
        next_monday = now + timedelta(days=(7 - now.weekday()))
        self.scheduler.schedule(self.update_regulars(), next_monday)
    """


def setup(bot):
    bot.add_cog(RegularAssigner(bot))
