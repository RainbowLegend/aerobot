import discord
import asyncio
import json
from discord.ext import commands
from datetime import datetime, timedelta


class RegularAssigner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def activity_check(messages: list, time_sep: int):
        messages = [x for x in messages if x.channel.id not in [702603189324873768, 748238536636891217]]
        message_total = 0
        last_time = datetime.now()
        for message in messages:
            if abs((message.created_at - last_time).seconds) > (time_sep * 60):
                last_time = message.created_at
                message_total += 1
        return message_total

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(702600628601356359)

        now = datetime.now()
        week_ago = datetime.utcnow() - timedelta(days=7)
        channels = [702601830013599814, 702602469812863106, 717090761056976948, 702602837737078897, 702603094189670483,
                    702600628601356362, 702603144693022751, 702603364575346769, 702603823620816946]
        # tos-general, gamenights, ranked-lounge, tos-matches, trial-reports, general, flummery, pets, art
        server_history = []
        for channel in channels:
            print(channel, "starting")
            channel_history = await (guild.get_channel(channel)).history(after=week_ago, limit=None).flatten()
            server_history = server_history + channel_history
            print(len(channel_history), channel)
        print(len(server_history))
        _2min = 0
        _2min45 = 0
        _3min = 0
        _3min45 = 0
        for member in guild.members:
            activity = [message for message in server_history if message.author == member]
            message_total = self.activity_check(activity, 2)
            if message_total >= 45:
                _2min45 += 1
            if message_total >= 60:
                _2min += 1
            message_total = self.activity_check(activity, 3)
            if message_total >= 60:
                _3min += 1
            if message_total >= 45:
                _3min45 += 1
        print(_2min45, " 2m45")
        print(_2min, " 2m60")
        print(_3min45, " 3m45")
        print(_3min, " 3m60")
        print(datetime.now() - now)


def setup(bot):
    bot.add_cog(RegularAssigner(bot))
