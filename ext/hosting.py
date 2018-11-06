import discord
from discord.ext import commands


class Notifications:
    """General notifier commands."""

    def __init__(self, bot):
        self.bot = bot
        self.toscd = bot.get_guild(288455332173316106)

    @commands.command()
    async def host(self, ctx, mode, notification_type, gamemode='Not Defined'):
        """Pings the appropriate role for the appropriate game mode.

        Params:
        mode - Either `Coven` or `Classic`
        notification_type - Either `start` or `final`
        gamemode - Things like Ranked Practice, Classic, etc.
        """

        coven = self.toscd.get_role(358655924342095874)
        classic = self.toscd.get_role(379748801197637644)

        start = ('{0.mention} **||** A new game of **{1}** is starting.\n\n'
                 'Use `/joingame [ToS IGN]` or `/jg [ToS IGN]` to join. You will shortly get a party '
                 'invite.')
        final = ('{0.mention} **||** A new game of **{1}** is starting.\nThe game will start shortly.\n\n'
                 'Use `/joingame [ToS IGN]` or `/jg [ToS IGN]` to join. You will shortly get a party '
                 'invite.')

        if notification_type.lower() == 'start':
            msg = start
        elif notification_type.lower() == 'final':
            msg = final

        if mode.lower() == 'coven':
            return await ctx.send(msg.format(coven, gamemode))
        elif mode.lower() == 'classic':
            return await ctx.send(msg.format(classic, gamemode))
        else:
            return await ctx.send('That is an invalid mode.', delete_after=5)

    @commands.command(name='joingame', aliases=['jg'])
    async def _joingame(self, ctx, ign):
        """Send your IGN to the lobby host."""

        await (self.toscd.get_channel(407003125128495104)).send(f'{ctx.author.mention} - **{ign}**')
        return await ctx.send(f'{ctx.author.mention}, your IGN was sent.')


def setup(bot):
    bot.add_cog(Notifications(bot))
