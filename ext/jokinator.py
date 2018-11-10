import discord
from discord.ext import commands
from jokes import JOKES


class Jokinator:
    """Let's make jokes!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dadjoke(self, ctx):
        """Polly want a dadjoke?"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}) as r:
                raw_joke = await r.json()
            joke = raw_joke['joke']
            await ctx.send(f'{ctx.message.author.mention}, {joke}')

    @commands.command()
    async def givejoke(self, ctx):
        """Want cool jokes?"""
        await ctx.send(f'{ctx.message.author.mention}, {random.choice(JOKES)}')
        
    async def on_message(self, message):
      """This method is used for the dabs."""
      if any(map(lambda v: v in message.content, [';dab;', '!dab'])):
        return await message.channel.send('<a:eli1:472941813011972107><a:eli2:472941813229944842><a:eli3:472941813267824670>')


def setup(bot):
    bot.add_cog(Jokinator(bot))
