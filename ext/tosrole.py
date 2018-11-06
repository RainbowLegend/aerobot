import discord
from discord.ext import commands


class SelfRoles:
    """This cog is used for people who want their own roles in the TOSCD."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tosrole(self, ctx, *, newrole):
        """Y'all like jazz?"""

        toscd = self.bot.get_guild(288455332173316106)
        base_roles = {
            'town': toscd.get_role(297159204181901323),
            'mafia': toscd.get_role(297159278303641600),
            'neutral_killing': toscd.get_role(297169993270034433),
            'neutral_benign': toscd.get_role(297170017634746369),
            'neutral_evil': toscd.get_role(297170044553789440),
            'neutral_chaos': toscd.get_role(297170076002680840),
            'coven': toscd.get_role(291745541581307904)
        }

        roles = {
            'jailor': [base_roles['town'], toscd.get_role(289508430350254080)],
            'veteran': [base_roles['town'], toscd.get_role(291743946642554883)],
            'vigilante': [base_roles['town'], toscd.get_role(291743984525770754)],
            'vampirehunter': [base_roles['town'], toscd.get_role(291743908306616323)],
            'investigator': [base_roles['town'], toscd.get_role(291743168515538946)],
            'lookout': [base_roles['town'], toscd.get_role(291743325814521856)],
            'sheriff': [base_roles['town'], toscd.get_role(291743280813703168)],
            'spy': [base_roles['town'], toscd.get_role(291743388661841920)],
            'psychic': [base_roles['town'], toscd.get_role(321785338987282432)],
            'tracker': [base_roles['town'], toscd.get_role(321785330439159818)],
            'escort': [base_roles['town'], toscd.get_role(291743471750873088)],
            'mayor': [base_roles['town'], toscd.get_role(291743563711250442)],
            'medium': [base_roles['town'], toscd.get_role(291743513182208000)],
            'retributionist': [base_roles['town'], toscd.get_role(291743627489574912)],
            'transporter': [base_roles['town'], toscd.get_role(291743680241336321)],
            'doctor': [base_roles['town'], toscd.get_role(291743828849852416)],
            'bodyguard': [base_roles['town'], toscd.get_role(291743751846494208)],
            'crusader': [base_roles['town'], toscd.get_role(321785124230397952)],
            'trapper': [base_roles['town'], toscd.get_role(321785341340286976)],

            'godfather': [base_roles['mafia'], toscd.get_role(289509219214950400)],
            'mafioso': [base_roles['mafia'], toscd.get_role(291744083750158357)],
            'ambusher': [base_roles['mafia'], toscd.get_role(321786150916194304)],
            'blackmailer': [base_roles['mafia'], toscd.get_role(291744254563319809)],
            'consigliere': [base_roles['mafia'], toscd.get_role(291744342572269568)],
            'consort': [base_roles['mafia'], toscd.get_role(291744422213844992)],
            'disguiser': [base_roles['mafia'], toscd.get_role(291744520469610496)],
            'forger': [base_roles['mafia'], toscd.get_role(291744553919184897)],
            'framer': [base_roles['mafia'], toscd.get_role(291744602090897408)],
            'janitor': [base_roles['mafia'], toscd.get_role(291744671292456960)],
            'hypnotist': [base_roles['mafia'], toscd.get_role(321786146835267594)],

            'arsonist': [base_roles['neutral_killing'], toscd.get_role(291744786275106817)],
            'serialkiller': [base_roles['neutral_killing'], toscd.get_role(291745200328671243)],
            'werewolf': [base_roles['neutral_killing'], toscd.get_role(291745330574393344)],
            'juggernaut': [base_roles['neutral_killing'], toscd.get_role(326914566263013386)],

            'executioner': [base_roles['neutral_evil'], toscd.get_role(289509291306647552)],
            'jester': [base_roles['neutral_evil'], toscd.get_role(291745484681510922)],
            'witch': [base_roles['neutral_evil'], toscd.get_role(400981824706445328)],

            'amnesiac': [base_roles['neutral_benign'], toscd.get_role(291745696707772417)],
            'survivor': [base_roles['neutral_benign'], toscd.get_role(291745801107931142)],
            'guardianangel': [base_roles['neutral_benign'], toscd.get_role(321785643812388864)],

            'vampire': [base_roles['neutral_chaos'], toscd.get_role(291746016418594827)],
            'pirate': [base_roles['neutral_chaos'], toscd.get_role(321785635956588544)],
            'plaguebearer': [base_roles['neutral_chaos'], toscd.get_role(321786136974458921)],
            'pestilence': [base_roles['neutral_chaos'], toscd.get_role(326914120576270347)],
            'baker': [base_roles['neutral_chaos'], toscd.get_role(288682060414058516)],

            'covenleader': [base_roles['coven'], toscd.get_role(321784224866631690)],
            'hexmaster': [base_roles['coven'], toscd.get_role(321784193451556866)],
            'medusa': [base_roles['coven'], toscd.get_role(321784220240314370)],
            'necromancer': [base_roles['coven'], toscd.get_role(321784223608340480)],
            'poisoner': [base_roles['coven'], toscd.get_role(321784203127816193)],
            'potionmaster': [base_roles['coven'], toscd.get_role(321784216075501569)],
        }
        if ctx.channel.id not in [288463362357067777, 288455332173316106, 296069608216068098]:
            return await ctx.send(f'{ctx.author.mention} **||** This command is only usable in '
                                  '<#288455332173316106> or <#288463362357067777>.')
        elif newrole.lower() not in roles.keys():
            return await ctx.send(f'{ctx.author.mention} **||** For a list of roles, please check '
                                  '<#288752291463299083>.  Make sure capitalization is also followed.')

        for role in roles.values():
            if role[1].id in (crole.id for crole in ctx.author.roles):
                await ctx.author.remove_roles(*role, reason='Auto assigner (removal)')

        await ctx.author.add_roles(*roles[newrole.lower()], reason='Auto assigner')

        await ctx.send(f'{ctx.author.mention}, you have been assigned **{roles[newrole.lower()][1].name.title()}**')

    @commands.command()
    async def nsfw(self, ctx):
        """Gives you the NSFW role."""
        toscd = self.bot.get_guild(336642139381301249)
        nsfw = toscd.get_role(425123783863435276)
        if nsfw in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfw, reason='NSFW removal')
            await ctx.send(f"{ctx.author.mention}, you have been unassigned the NSFW role.")
            return
        else:
            await ctx.author.add_roles(nsfw, reason='NSFW addition')
            return await ctx.send(f"{ctx.author.mention}, you have been assigned the NSFW role.")

    @commands.command()
    async def gnotif(self, ctx, arg=None):
        """Notifications for games

        arg must be either 'enable' or 'disable'"""

        toscd = self.bot.get_guild(336642139381301249)
        role = toscd.get_role(379748801197637644)

        if ctx.channel.id in [288463362357067777, 288455332173316106, 296069608216068098]:
            if arg.lower() not in ['enable', 'disable']:
                return await ctx.send('Use either `/gnotif enable` to enable notifcations or '
                                      '`/gnotif disable` to disable notifications.')

            elif arg.lower() == 'enable':
                await ctx.send(f'{ctx.author.mention}, you will now **recieve** game notifications. Use `/gnotif '
                               f'disable` to *disable* them.')
                return ctx.author.add_roles(role, reason='GN auto-assign')

            elif arg.lower() == 'disable':
                await ctx.send(f'{ctx.author.mention}, You will now **not** recieve game notifications. '
                               f'Use `/gnotif enable` to *enable* them.')

        else:
            return await self.bot.say(f'{ctx.author.id} **||** This command is only usable in '
                                      '<#288455332173316106> or <#288463362357067777>.')

    @commands.command()
    async def coven(self, ctx, arg=None):
        """Notifications for coven games

        arg must be either 'enable' or 'disable'
        """

        toscd = self.bot.get_guild(336642139381301249)
        role = toscd.get_role(358655924342095874)

        if ctx.channel.id in [288463362357067777, 288455332173316106, 296069608216068098]:
            if arg.lower() not in ['enable', 'disable']:
                return await ctx.send('Use either `/coven enable` to enable coven notifcations or '
                                      '`/coven disable` to disable notifications.')

            elif arg.lower() == 'enable':
                await ctx.send(f'{ctx.author.mention}, you will now **recieve** coven notifications. Use `/coven '
                               f'disable` to *disable* them.')
                return ctx.author.add_roles(role, reason='GN auto-assign')

            elif arg.lower() == 'disable':
                await ctx.send(f'{ctx.author.mention}, You will now **not** recieve coven notifications. '
                               f'Use `/coven enable` to *enable* them.')

        else:
            return await self.bot.say(f'{ctx.author.id} **||** This command is only usable in '
                                      '<#288455332173316106> or <#288463362357067777>.')


def setup(bot):
    n = SelfRoles(bot)
    bot.add_cog(n)
