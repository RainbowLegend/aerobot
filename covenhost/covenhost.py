import discord
from discord.ext import commands
import os


class CovenHost:
    """Self ToS Role assignment system. ~Danners"""

    default = {}

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def coven(self, ctx):
        """Notifications for games"""

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)
        covennotifs = discord.Role(id='358655924342095874', server='288455332173316106')
        senior = discord.Role(id='288464565791096838', server='288455332173316106')
        mod = discord.Role(id='288682024515141634', server='288455332173316106')
        gmn = discord.Role(id='358401178909933568', server='288455332173316106')
        temp = discord.Role(id='465973033106931713', server='288455332173316106')

        if channelid in ['358331904233046016', '358660402462326784', '288463362357067777', '288455332173316106',
                         '296069608216068098']:
            if ctx.invoked_subcommand is None:
                if senior or mod or gmn or temp in ctx.message.author.roles:
                    await self.bot.say('`/coven host` or `/coven final` or `/coven gamemodes`')
                elif covennotifs in ctx.message.author.roles:
                    await self.bot.say('Use `/coven disable` to disable Coven Notifications.')
                else:
                    await self.bot.say('Use `/coven enable` to enable Coven Notifications.')
        else:
            await self.bot.say(f'{ctx.message.author.mention} **||** This command is only usable in <#288455332173316106> or '
                                                 '<#288463362357067777>.')
            return

    @coven.command(pass_context=True)
    async def enable(self, ctx):
        channel = ctx.message.channel
        channelid = str(channel.id)

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            await self.bot.say(f"{ctx.message.author.mention} **||** This command is only usable in <#288455332173316106>, "
                               f"<#288463362357067777> or <#358331904233046016>.")
            return

        user = ctx.message.author
        optinrole = discord.Role(id='358655924342095874', server='288455332173316106')

        await self.bot.add_roles(user, optinrole)
        await self.bot.say('You will now **recieve** coven game notifications. Use `/coven disable` to *disable* them.')

    @coven.command(pass_context=True)
    async def disable(self, ctx):
        channel = ctx.message.channel
        channelid = str(channel.id)

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            await self.bot.say("<@" + str(ctx.message.author.id) + "> **||** This command is only usable in "
                                                                   "<#288455332173316106>, <#288463362357067777> or "
                                                                   "<#358331904233046016>.")
            return

        user = ctx.message.author
        optinrole = discord.Role(id='358655924342095874', server='288455332173316106')

        await self.bot.remove_roles(user, optinrole)
        await self.bot.say(
            'You now **will not** recieve coven game notifications. Use `/coven enable` to *enable* them.')

    @coven.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def host(self, ctx, *, gamemode = None):
        """Notify a game is starting"""

        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='358655924342095874', server='288455332173316106')

        if gamemode is None:
            gamemode = "Not defined"

        gamemode = str(gamemode)
        auth = str(ctx.message.author.id)

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                                 colour=discord.Colour(0x550a94), mentionable=True)

        await self.bot.say(f"<@&358655924342095874> **||** A new game of ** {gamemode}** is starting.\n\n"
                           "Use `/joingame [Town of Salem IGN]` or `/jg [ToS IGN]` to join. You will shortly after "
                           "get a party invite.")

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                                 colour=discord.Colour(0x550a94), mentionable=False)

        await self.bot.send_message(self.bot.get_channel('407003125128495104'), "Names for the game of **"
                                    + str(gamemode) + "** are being posted below.")

    @coven.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def final(self, ctx, *, gamemode):
        """Notify a game is starting"""

        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='358655924342095874', server='288455332173316106')

        if gamemode is None:
            gamemode = "Not defined"

        gamemode = str(gamemode)
        auth = str(ctx.message.author.id)

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                           colour=discord.Colour(0x550a94), mentionable=True)

        await self.bot.say(f"<@&358655924342095874> **||** This is the final call for a game of **{gamemode}** is "
                           f"starting.\n"
                            "The game will start shortly.\n\n"
                            "Use `/joingame [Town of Salem IGN]` or `/jg [ToS IGN]` to join. You will shortly after "
                            "get a party invite.")

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                           colour=discord.Colour(0x550a94), mentionable=False)

    @coven.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def gamemodes(self, ctx):
        """Vote for today's gamemodes"""

        toscd = discord.Server(id='288455332173316106')
        emoteLib = discord.Server(id='401122122400923648')
        optinrole = discord.Role(id='358655924342095874', server='288455332173316106')

        auth = str(ctx.message.author.id)

        animpartyblob1 = discord.Emoji(name='animpartyblob1', server=emoteLib)

        classic = discord.Emoji(id='406242997852700672', server=toscd)
        rp = discord.Emoji(id='406242997903163392', server=toscd)
        custom = discord.Emoji(id='406242997584396299', server=toscd)
        eve = discord.Emoji(id='406242997492252674', server=toscd)
        rm = discord.Emoji(id='406242997727133697', server=toscd)
        aa = discord.Emoji(id='406242998205153298', server=toscd)
        mr = discord.Emoji(id='406242998083649546', server=toscd)

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                                 colour=discord.Colour(0x550a94), mentionable=True)

        msg = await self.bot.say("<a:animpartyblob1:401122373236948993> <a:animpartyblob2:401122373367234570> <a:animpartyblob3:401122373396463616> <a:animpartyblob4:401122373262376971> <a:animpartyblob5:401122373425823744> <a:animpartyblob6:401122373614567434> <a:animpartyblob7:401122373698322432> <a:animpartyblob8:401122373270503427> <a:animpartyblob9:401122373434343431>\n"
                                 "<@&358655924342095874> **||** We're voting for today's coven gamemodes! "
                                 "React to a gamemode to react.\nYou may choose more than 1.\n\n"
                                 "**You may choose from these options:**\n"
                                 "<:CovenNormalClassic:406242997852700672> - Classic.\n"
                                 "<:CovenRankedPractice:406242997903163392> - Ranked Practice.\n"
                                 "<:CovenCustomCustom:406242997584396299> - Custom.\n"
                                 "<:CovenEvilsVEvils:406242997492252674> - Evils v Evils.\n"
                                 "<:CovenAllAny:406242997727133697> - All Any.\n"
                                 "<:CovenMafiaReturns:406242998083649546> - Mafia Returns.\n"
                                 "<:CovenRotating:406242998205153298> - Rotating Gamemode (VIP or Lovers.)")

        await self.bot.edit_role(toscd, optinrole, name="Coven Notifications",
                                 colour=discord.Colour(0x550a94), mentionable=False)

        await self.bot.add_reaction(msg, classic)
        await self.bot.add_reaction(msg, rp)
        await self.bot.add_reaction(msg, custom)
        await self.bot.add_reaction(msg, eve)
        await self.bot.add_reaction(msg, rm)
        await self.bot.add_reaction(msg, mr)
        await self.bot.add_reaction(msg, aa)


def setup(bot):
    n = CovenHost(bot)
    bot.add_cog(n)
