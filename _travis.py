from discord.ext import commands
import logging


class Config:
    token = "HI"
    extensions = ['ext.auth', 'ext.cleverbot', 'ext.hosting', 'ext.ir_emb', 'ext.jokinator', 'ext.misc', 'ext.moderation', 'ext.owner', 'ext.tosrole']


config = Config


class AeroBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_extensions(self, extensions):
        for extension in extensions:
            self.load_extension(extension)


bot = AeroBot(command_prefix='/', case_insensitive=True)
bot.load_extensions(config.extensions)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print("Travis Tests Successful!")
# test
