import discord

class NewEmotes:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if "!dab" in message.content or ";dab;" in message.content:
            await self.bot.send_message(message.channel, "<a:eli1:472941813011972107><a:eli2:472941813229944842><a:eli3:472941813267824670>")

def setup(bot):
    bot.add_cog(NewEmotes(bot))
