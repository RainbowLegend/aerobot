from discord.ext import commands


class Auth:
    """Authorization command for the official TOSCD."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def auth(self, ctx):
        destination = self.bot.get_channel(288677420720979978)
        inv = await destination.create_invite(reason='Auth server', max_uses=1, max_age=60, unique=True)
        await ctx.author.send(f'Your unique invite link is: {inv}')


def setup(bot):
    bot.add_cog(Auth(bot))