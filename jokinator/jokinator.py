import discord
from discord.ext import commands
import aiohttp
import random

JOKES = [
    "Yeet this is elijah's test."
]


class Jokinator:
    """Let's make jokes!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dadjoke(self, ctx):
        """Polly want a dadjoke?"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}) as r:
                raw_joke = await r.json()
            joke = raw_joke['joke']
            await self.bot.say(f'{ctx.message.author.mention}, {joke}')

    @commands.command(pass_context=True)
    async def givejoke(self, ctx):
        """Want cool jokes?"""
        await self.bot.say(f'{ctx.message.author.mention}, {random.choice(JOKES)}')


def setup(bot):
    bot.add_cog(Jokinator(bot))
