import typing
from discord.ext import commands
import discord
from consts import COVEN, CLASSIC, VOTE, START, FINAL, GAMEMODES


class Hosting(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # /host

    @commands.command(name='host')
    @commands.has_any_role(702601007368241173, 702604059613462589, 702604111450996818, 702605281204502638)
    async def host(self, ctx, mode, notification_type, *, gamemode='Not Defined'):

        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)

        coven = guild.get_role(702610491717189673)
        classic = guild.get_role(702609120540491786)

        if notification_type.lower() == 'start':
            msg = START
        elif notification_type.lower() == 'final':
            msg = FINAL

        if gamemode.lower() not in GAMEMODES:
            return await ctx.send('That is an invalid gamemode.', delete_after=5)
        
        channel = guild.get_channel(702639694474903643)
        
        if mode.lower() == 'coven':
            await coven.edit(reason="hosting mentions", mentionable=True)
            await ctx.send(msg.format(coven, gamemode))
            await channel.send(f"**{ctx.author.display_name}'s {gamemode} Game**".upper())
            return await coven.edit(reason="hosting mentions", mentionable=False)
        elif mode.lower() == 'classic':
            await classic.edit(reason="hosting mentions", mentionable=True)
            await ctx.send(msg.format(classic, gamemode))
            await channel.send(f"**{ctx.author.display_name}'s {gamemode} Game**".upper())
            return await classic.edit(reason="hosting mentions", mentionable=False)
        else:
            return await ctx.send('That is an invalid mode.', delete_after=5)

    # /joingame

    @commands.command(name='joingame', aliases=['jg', 'join'])
    async def joingame(self, ctx, ign=None):
        """Send your IGN to the lobby host."""
        await ctx.message.delete()

        guild = self.bot.get_guild(702600628601356359)
        if ign:
            await (guild.get_channel(702639694474903643)).send(f'**`{discord.utils.escape_mentions(ign.capitalize())}`** ({ctx.author.mention})')
            return await ctx.send(f'{discord.utils.escape_mentions(ign.capitalize())} will receive a party invite shortly. ({ctx.author.mention})')
        else:
            return await ctx.send(f'You didn\'t provide your ign! ({ctx.author.mention})')

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
            await res.add_reaction('Coven_Classic:772315471235776513')
            await res.add_reaction('Coven_RankedPractice:772315471248228352')
            await res.add_reaction('Coven_MafiaReturns:772315471202091029')
            await res.add_reaction('Coven_Custom:772315471285452810')
            await res.add_reaction('Coven_AllAny:772315471332376616')
            await res.add_reaction('Coven_Rotating:772315471235645461')
        elif mode.lower() == 'classic':
            res = await ctx.send(CLASSIC)
            await res.add_reaction('Classic_Classic:772315471277981706')
            await res.add_reaction('Classic_RankedPractice:772315471164211221')
            await res.add_reaction('Classic_Custom:772315471381921812')
            await res.add_reaction('Custom_Rapid:772315471289647124')
            await res.add_reaction('Classic_AllAny:772315471323856908')
            await res.add_reaction('Classic_Rainbow:772315471432253450')
            await res.add_reaction('Classic_DraculasPalace:772315471424389120')
            await res.add_reaction('Classic_TownTraitor:772315471378513930')
        elif mode.lower() == 'vote':
            res = await ctx.send(VOTE)
            await res.add_reaction('Classic_Icon:772315471403679765')
            await res.add_reaction('Coven_Icon:772315471340371968')
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
            return await ctx.send(f'Gamenight ended! ({ctx.author.mention})\nIf you wish to continue playing, you can organize your own games in <#702602837737078897>.')

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
    bot.add_cog(Hosting(bot))
