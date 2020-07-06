import typing
from discord.ext import commands
import discord
from consts import COVEN, CLASSIC, VOTE, START, FINAL


class Notifications(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # /host

    @commands.command(name='host')
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
    async def host(self, ctx, mode, notification_type, *, gamemode='Not Defined'):
        """Pings the appropriate role for the appropriate game mode.
        Params:
        mode - Either `Coven` or `Classic`
        notification_type - Either `start` or `final`
        gamemode - Things like Ranked Practice, Classic, etc.
        """
        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)

        coven = guild.get_role(702610491717189673)
        classic = guild.get_role(702609120540491786)

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
            "caa",
            "coven any all",
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
    async def _joingame(self, ctx, ign: None):
        """Send your IGN to the lobby host."""
        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)
        if ign == None:
            return await ctx.send(f'You didn\'t provide your ign! ({ctx.author.mention})')
        else:
            await (guild.get_channel(702639694474903643)).send(f'{ctx.author.mention} - **{ign}**')
            return await ctx.send(f'{ign.capitalize()} will receive a party invite shortly. ({ctx.author.mention})')

    # /gamemodes

    @commands.command(name='gamemodes')
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
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

  # /end

    @commands.command(name="end")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
    async def end(self, ctx, cohost: typing.Optional[discord.User]):
        guild = self.bot.get_guild(702600628601356359)
        await ctx.message.delete()
        await guild.get_channel(702602469812863106).set_permissions(guild.get_role(702694502204178554), send_messages=False)
        if cohost:
            return await ctx.send(f'Gamenight ended! ({ctx.author.mention}, {cohost.mention})\nIf you wish to continue playing, you can organize your own games in <#702602837737078897>.')
        else:
            return await ctx.send(f'Gamenight opened! ({ctx.author.mention})\nIf you wish to continue playing, you can organize your own games in <#702602837737078897>.')

  # /start

    @commands.command(name="start")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
    async def start(self, ctx, cohost: typing.Optional[discord.User]):
        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)
        await guild.get_channel(702602469812863106).set_permissions(guild.get_role(702694502204178554), send_messages=True)
        if cohost:
            return await ctx.send(f'Gamenight opened! ({ctx.author.mention}, {cohost.mention})')
        else:
            return await ctx.send(f'Gamenight opened! ({ctx.author.mention})')

  # /takeover

    @commands.command(name="takeover")
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
    async def takeover(self, ctx, cohost: typing.Optional[discord.User]):
        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)
        if cohost:
            return await ctx.send(f'Gamenight takeover. ({ctx.author.mention}, {cohost.mention})')
        else:
            return await ctx.send(f'Gamenight takeover. ({ctx.author.mention})')


def setup(bot):
    bot.add_cog(Notifications(bot))
