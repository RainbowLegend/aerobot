from discord.ext import commands


class Auth(commands.Cog):
  # Create one-time use invite links.

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="auth", hidden=True)
    @commands.enabled(False)
    async def auth(self, ctx):
        destination = self.bot.get_channel(288677420720979978)
        inv = await destination.create_invite(reason='Auth server', max_uses=1, max_age=60, unique=True)
        await ctx.author.send(f'Your unique invite link is: {inv}')


def setup(bot):
    bot.add_cog(Auth(bot))
