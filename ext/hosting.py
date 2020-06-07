from discord.ext import commands
from ext.consts import COVEN, CLASSIC


class Notifications(commands.Cog):
    """General notifier commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Senior Moderator", "Gamenight Host", "Server Manager")
    async def host(self, ctx, mode, notification_type, *, gamemode='Not Defined'):
        """Pings the appropriate role for the appropriate game mode.
        Params:
        mode - Either `Coven` or `Classic`
        notification_type - Either `start` or `final`
        gamemode - Things like Ranked Practice, Classic, etc.
        """
        
        toscd = self.bot.get_guild(702600628601356359)

        coven = toscd.get_role(702610491717189673)
        classic = toscd.get_role(702609120540491786)

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
            await coven.edit(reason="hosting mentions", mentionable=True)
            await ctx.send(msg.format(coven, gamemode))
            return await coven.edit(reason="hosting mentions", mentionable=False)
        elif mode.lower() == 'classic':
            await classic.edit(reason="hosting mentions", mentionable=True)
            await ctx.send(msg.format(classic, gamemode))
            return await classic.edit(reason="hosting mentions", mentionable=False)
        else:
            return await ctx.send('That is an invalid mode.', delete_after=5)

    @commands.command(name='joingame', aliases=['jg'])
    async def _joingame(self, ctx, ign):
        """Send your IGN to the lobby host."""
        toscd = self.bot.get_guild(702600628601356359)
        await (toscd.get_channel(702639694474903643)).send(f'{ctx.author.mention} - **{ign}**')
        return await ctx.send(f'{ctx.author.mention}, your IGN was sent.')

    @commands.command(name='gamemodes')
    @commands.has_any_role("Administrator", "Moderator", "Senior Moderator", "Gamenight Host", "Server Manager")
    async def gamemodes(self, ctx, mode):
        """Sends the message for each gamemode.
        Params
        ========
        mode - `str` Either `coven` or `classic`"""
        if mode.lower() == 'coven':
            res = await ctx.send(COVEN)
            await res.add_reaction('CovenNormalClassic:702948620449742960')
            await res.add_reaction('CovenRankedPractice:702948620546342942')
            await res.add_reaction('CovenCustomCustom:702948620281970689')
            await res.add_reaction('CovenEvilsVEvils:702948620194021427')
            await res.add_reaction('CovenAllAny:702948620558663840')
            await res.add_reaction('CovenMafiaReturns:702948620571246643')
            await res.add_reaction('CovenRotating:702948620592349314')
        elif mode.lower() == 'classic':
            res = await ctx.send(CLASSIC)
            await res.add_reaction('NormalClassic:702948620596674620')
            await res.add_reaction('NormalRankedPractice:702948620676366436')
            await res.add_reaction('CustomCustom:702948620571246724')
            await res.add_reaction('CustomEvilsvEvils:702948620596412436')
            await res.add_reaction('CustomRapidMode:702948620554600498')
            await res.add_reaction('ChaosAllAny:702948620697075782')
            await res.add_reaction('ChaosRainbow:702948620546342982')
            await res.add_reaction('ChaosVigilantics:702948620252741754')
        else:
            await ctx.send('Invalid gamemode!')


def setup(bot):
    bot.add_cog(Notifications(bot))
