import discord
from discord.ext import commands


class Auth:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def auth(self, ctx):
        author = ctx.message.author
        destination = self.bot.get_server(id='288455332173316106')

        invite = await self.bot.create_invite(destination, max_uses=1, max_age=35)

        await self.bot.send_message(author, f'Your unique, one-use invite code is {invite}.')

    async def on_message(self, message):
        if message.server.id in ['288455332173316106', '488500791288528906']:
            if len(message.role_mentions) >= 3:
                if len(message.attachments) >= 1:
                    await self.bot.send_message(message.author, 'You have been kicked for mentioning all staff.\n'
                                                                'You may rejoin if you wish.')
                    await self.bot.send_message(self.bot.get_channel('288681936870703105'),
                                                f'{message.author.mention} has been kicked for autospam. '
                                                '(3+ role ping, attachment)')
                    await self.bot.kick(message.author)
            elif len(message.role_mentions) >= 4:
                await self.bot.send_message(message.author, 'You have been kicked for mentioning all staff.\n'
                                                            'You may rejoin if you wish.')
                await self.bot.send_message(self.bot.get_channel('288681936870703105'),
                                            f'{message.author.mention} has been kicked for autospam. (4+ role ping)')
                await self.bot.kick(message.author)


def setup(bot):
    n = Auth(bot)
    bot.add_cog(n)
