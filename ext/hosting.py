import discord
from discord.ext import commands


class Notifications:
    """General notifier commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def host(self, ctx, mode, notification_type, gamemode='Not Defined'):
        """Pings the appropriate role for the appropriate game mode.
        Params:
        mode - Either `Coven` or `Classic`
        notification_type - Either `start` or `final`
        gamemode - Things like Ranked Practice, Classic, etc.
        """
        
        toscd = self.bot.get_guild(288455332173316106)

        coven = toscd.get_role(358655924342095874)
        classic = toscd.get_role(379748801197637644)

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
            res = await ctx.send(msg.format(coven, gamemode))
            await res.add_reaction('CovenNormalClassic:406242997852700672')
            await res.add_reaction('CovenRankedPractice:406242997903163392')
            await res.add_reaction('CovenCustomCustom:406242997584396299')
            await res.add_reaction('CovenEvilsVEvils:406242997492252674')
            await res.add_reaction('CovenAllAny:406242997727133697')
            await res.add_reaction('CovenMafiaReturns:406242998083649546')
            await res.add_reaction('CovenRotating:406242998205153298')
        elif mode.lower() == 'classic':
            res = await ctx.send(msg.format(classic, gamemode))
            await res.add_reaction('NormalClassic:386748316894887938')
            await res.add_reaction('NormalRankedPractice:386742079252070401')
            await res.add_reaction('CustomCustom:386742078975115265')
            await res.add_reaction('CustomEvilsvEvils:386742078912069633')
            await res.add_reaction('CustomRapidMode:386748316886499328')
            await res.add_reaction('ChaosAllAny:386742078421467159')
            await res.add_reaction('ChaosRainbow:386742078845222937')
            await res.add_reaction('ChaosVigilantics:386742078471667714')
        else:
            return await ctx.send('That is an invalid mode.', delete_after=5)

    @commands.command(name='joingame', aliases=['jg'])
    async def _joingame(self, ctx, ign):
        """Send your IGN to the lobby host."""
        self.bot.get_guild(288455332173316106)
        await (toscd.get_channel(407003125128495104)).send(f'{ctx.author.mention} - **{ign}**')
        return await ctx.send(f'{ctx.author.mention}, your IGN was sent.')


def setup(bot):
    bot.add_cog(Notifications(bot))
