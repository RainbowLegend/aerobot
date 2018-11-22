import discord
from discord.ext import commands
import aiohttp
import typing


class CleverBot:
    """Some random ***intelligent*** commands

    You can interact with the bot by pinging it with a question."""

    def __init__(self, bot):
        self.bot = bot
        self.context = {}
        self.key = ""

    async def on_message(self, message):
        """This is for processing the CleverBot responses."""

        if str(self.bot.user.id) in message.content.split(" ")[0]:
            text = " ".join(message.content.split(" ")[1:])
            if not (3 <= len(text) <= 60):
                return await message.channel.send("Text must be between 3-60 characters.")

            if str(message.author.id) not in self.context.keys():
                self.context[str(message.author.id)] = []

            payload = {
                "text": text,
                "context": self.context[str(message.author.id)]
            }

            self.context[str(message.author.id)].append(text)
            
            if len(self.context[str(message.author.id)]) > 2:
                self.context[str(message.author.id)].pop(0)

            async with message.channel.typing(), aiohttp.ClientSession() as cs:
                req = await cs.post("https://public-api.travitia.xyz/talk", json=payload,
                                    headers={"authorization": self.key})
                await message.channel.send((await req.json())["response"])

    @commands.command()
    @commands.is_owner()
    async def updatekey(self, ctx, *, key):
        self.key = key

        await ctx.send(f'ok, key is now `{self.key}`')

    @commands.command()
    async def snipe(self, ctx, timeout: typing.Optional[int] = 300):
        """Snipes the next message!

        Default timeout is 300 seconds."""

        await ctx.send('Sniping in this channel...', delete_after=5)

        def check(m):
            return m.channel.id == ctx.channel.id and m.author.id == self.bot.user.id

        try:
            message = await self.bot.wait_for('message_delete', timeout=timeout, check=check)
        except asyncio.TimeoutError:
            return await ctx.author.send('Your sniper timed out!')

        em = discord.Embed(colour=discord.Colour.red(), description=message.content)
        em.set_author(name=f'{message.author} said...', icon_url=message.author.avatar_url)

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(CleverBot(bot))
