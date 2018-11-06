import discord
from discord.ext import commands
import random
from config import lelijah


class Miscellaneous:
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def penis(self, ctx, user: discord.Member=None):
        """:b:enis?"""
        if user.id == 228700305263558656:
            return await self.bot.say(lelijah)
        elif user is None:
            user = ctx.author
        state = random.getstate()
        random.seed(user.id)
        random.setstate(state)
        await self.bot.say(f"Size: 8{'=' * random.randint(0, 30)}D")


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
