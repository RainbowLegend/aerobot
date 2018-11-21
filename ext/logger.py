import discord
from discord.ext import commands
from time import strftime
import typing


class MessageLogger:
    """Logs messages in our server!"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        """This processes each message sent in our server"""
        if not message.guild:  # Server only, idrc if you send gay porn to the bot. Nor do I want to see it.
            self.bot.process_command(message)
            return
        
        channel = message.channel

        time = message.created_at.strftime("%Y-%b-%d %H:%M:%S")

        with open(f'logs/channels/{channel.id}.log', 'a+') as f:
            f.write(f'{time} {message.author} || {message.content}')

            if message.attachments:
                f.write(f'Additional attachments: {a.url for a in message.attachments}')
                
        with open(f'logs/users/{message.author.id}.log', 'a+') as f:
            f.write(f'{time} {message.channel} || {message.content}')

            if message.attachments:
                f.write(f'Additional attachments: {a.url for a in message.attachments}')
        
        self.bot.process_command(message)

    @commands.command()
    @commands.has_any_role('Administrator', 'Senior Moderator', 'Moderator')
    async def log(self, ctx, target: typing.Union[discord.User, discord.TextChannel]):
        """Gets the logs for a user/channel.
        
        Params:
        target - `User` or `TextChannel` Where you want the logs from"""
        
        if isinstance(target, discord.User):
            await ctx.send(file=discord.File(f'logs/users/{target.id}.log', filename=target.name))
        
        elif isinstance(target, discord.TextChannel):
            await ctx.send(file=discord.File(f'logs/channels/{target.id}.log', filename=target.name))


def setup(bot):
    bot.add_cog(MessageLogger(bot))
