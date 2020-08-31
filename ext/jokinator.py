import aiohttp
import random
from discord.ext import commands
from consts import JOKES


class Jokinator(commands.Cog):
    """Let's make jokes!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dadjoke")
    async def dadjoke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}) as r:
                raw_joke = await r.json()
            joke = raw_joke['joke']
            await ctx.send(f'{ctx.message.author.mention}, {joke}')

    @commands.command(name="givejoke", aliases=["joke"])
    async def givejoke(self, ctx):
        await ctx.send(f'{ctx.message.author.mention}, {random.choice(JOKES)}')

    # This command is used for the dabs.
    @commands.command(name="dab")
    async def dab(self, ctx):
      ctx.send("<a:Aerobot_Dab_1:749791197224108043><a:Aerobot_Dab_2:749791187313098764><a:Aerobot_Dab_3:749791176063975504>")


def setup(bot):
    bot.add_cog(Jokinator(bot))
