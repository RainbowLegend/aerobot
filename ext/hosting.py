from discord.ext import commands
from consts import COVEN, CLASSIC, VOTE, START, FINAL


class Notifications(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # /host

    @commands.command(name='host')
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638, 724625915619049513)
    async def host(self, ctx, mode, notification_type, *, gamemode='Not Defined'):
        """Pings the appropriate role for the appropriate game mode.
        Params:
        mode - Either `Coven` or `Classic`
        notification_type - Either `start` or `final`
        gamemode - Things like Ranked Practice, Classic, etc.
        """
        await ctx.message.delete()

        toscd = self.bot.get_guild(723203635185451142)

        coven = toscd.get_role(724716280845697135)
        classic = toscd.get_role(724716296037597226)

        if notification_type.lower() == 'start':
            msg = START
        elif notification_type.lower() == 'final':
            msg = FINAL

        gamemodes = [
            "classic",
            "ranked practice",
            "rankedpractice",
            "ranked practise",
            "rankedpractise",
            "custom",
            "rapid mode",
            "rapidmode",
            "all any",
            "allany",
            "any all",
            "anyall",
            "rainbow",
            "dracula's palace",
            "draculas palace",
            "draculaspalace",
            "dracula'spalace",
            "town traitor",
            "towntraitor",
            "mafia returns",
            "mafiareturns",
            "vip",
            "lovers",
            "rotating gamemode",
            "rotatinggamemode"
        ]

        if gamemode.lower() not in gamemodes:
            return await ctx.send('That is an invalid gamemode.', delete_after=5)

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

    # /joingame

    @commands.command(name='joingame', aliases=['jg'])
    async def _joingame(self, ctx, ign):
        """Send your IGN to the lobby host."""
        toscd = self.bot.get_guild(702600628601356359)
        await (toscd.get_channel(702639694474903643)).send(f'{ctx.author.mention} - **{ign}**')
        return await ctx.send(f'{ctx.author.mention}, your IGN was sent.')

    # /gamemodes

    @commands.command(name='gamemodes')
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638, 724625915619049513)
    async def gamemodes(self, ctx, mode):
        """Sends the message for each gamemode.
        Params
        ========
        mode - `str` Either `coven` or `classic`"""
        await ctx.message.delete()

        if mode.lower() == 'coven':
            res = await ctx.send(COVEN)
            await res.add_reaction('Coven_Classic:723204853433761893')
            await res.add_reaction('Coven_RankedPractice:723204889332809821')
            await res.add_reaction('Coven_MafiaReturns:723204877458604156')
            await res.add_reaction('Coven_Custom:723204865639055370')
            await res.add_reaction('Coven_AllAny:723204840729346119')
            await res.add_reaction('Coven_Rotating:723204902121373747')
        elif mode.lower() == 'classic':
            res = await ctx.send(CLASSIC)
            await res.add_reaction('Classic_Classic:723204741278204006')
            await res.add_reaction('Classic_RankedPractice:723204796945006643')
            await res.add_reaction('Classic_Custom:723204754431279125')
            await res.add_reaction('Classic_RapidMode:723204808336736388')
            await res.add_reaction('Classic_AllAny:723204714132668498')
            await res.add_reaction('Classic_Rainbow:723204782369538088')
            await res.add_reaction('Classic_DraculasPalace:723204769111605350')
            await res.add_reaction('Classic_TownTraitor:723204820718321745')
        elif mode.lower() == 'vote':
            res = await ctx.send(VOTE)
            await res.add_reaction('Classic_Icon:724663517990355115')
            await res.add_reaction('Coven_Icon:724663284317290526')
        else:
            await ctx.send('Invalid options!')

    @commands.command(name="end")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638, 724625915619049513)
    async def end(self, ctx):
        toscd = self.bot.get_guild(723203635185451142)
        await ctx.message.delete()
        await ctx.channel.set_permissions(toscd.get_role(724708658608472178), send_messages=False)
        await ctx.send('This gamenight has ended, go to <#702602837737078897> if you wish to continue playing.')

    @commands.command(name="start")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638, 724625915619049513)
    async def start(self, ctx):
        toscd = self.bot.get_guild(723203635185451142)
        await ctx.message.delete()
        await ctx.channel.set_permissions(toscd.get_role(724708658608472178), send_messages=True)
        await ctx.send(f'Gamenight opened! ({ctx.author.mention})')

    @commands.command(name="takeover")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638, 724625915619049513)
    async def takeover(self, ctx):
        toscd = self.bot.get_guild(723203635185451142)
        await ctx.message.delete()
        await ctx.channel.set_permissions(toscd.get_role(724708658608472178), send_messages=True)
        await ctx.send(f'Gamenight takeover. ({ctx.author.mention})')


def setup(bot):
    bot.add_cog(Notifications(bot))
