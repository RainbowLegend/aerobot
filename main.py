import discord
from discord.ext import commands
import config


class AeroBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_extensions(self, extensions):
        for extension in extensions:
            self.load_extension(extension)


bot = AeroBot(command_prefix='/', case_insensitive=True)
bot.load_extensions(config.extensions)
bot.load_extension('jishaku')

@bot.event
async def on_message(self, message):
    await bot.process_commands(message)

bot.run(config.token)
