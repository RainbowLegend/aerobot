from discord.ext import commands


class SelfRoles(commands.Cog):
    """This cog is used for people who want their own roles in the TOSCD."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tosrole(self, ctx, *, newrole):
        """Y'all like jazz?"""

        toscd = self.bot.get_guild(702600628601356359)
        base_roles = {
            'town': toscd.get_role(702604255269355610),
            'mafia': toscd.get_role(702604336248913940),
            'neutral_killing': toscd.get_role(702604410215333978),
            'neutral_benign': toscd.get_role(702608855661543544),
            'neutral_evil': toscd.get_role(702609935669919875),
            'neutral_chaos': toscd.get_role(702604367802400838),
            'coven': toscd.get_role(702604367802400838)
        }

        roles = {
            'jailor': [base_roles['town'], toscd.get_role(702605931971608596)],
            'veteran': [base_roles['town'], toscd.get_role(702606280837300265)],
            'vigilante': [base_roles['town'], toscd.get_role(702606235588886549)],
            'vampirehunter': [base_roles['town'], toscd.get_role(702606377327132703)],
            'investigator': [base_roles['town'], toscd.get_role(702605669513298022)],
            'lookout': [base_roles['town'], toscd.get_role(702605806658519070)],
            'sheriff': [base_roles['town'], toscd.get_role(702605770721853442)],
            'spy': [base_roles['town'], toscd.get_role(702606204261892146)],
            'psychic': [base_roles['town'], toscd.get_role(702607505339056169)],
            'tracker': [base_roles['town'], toscd.get_role(702607562662609057)],
            'escort': [base_roles['town'], toscd.get_role(702605954050424994)],
            'mayor': [base_roles['town'], toscd.get_role(702606063446393004)],
            'medium': [base_roles['town'], toscd.get_role(702606095583150163)],
            'retributionist': [base_roles['town'], toscd.get_role(702606144241270897)],
            'transporter': [base_roles['town'], toscd.get_role(702606313430974575)],
            'doctor': [base_roles['town'], toscd.get_role(702605844747124856)],
            'bodyguard': [base_roles['town'], toscd.get_role(702605897926443118)],
            'crusader': [base_roles['town'], toscd.get_role(702607601308925995)],
            'trapper': [base_roles['town'], toscd.get_role(702607654224134154)],

            'godfather': [base_roles['mafia'], toscd.get_role(702606921630482492)],
            'mafioso': [base_roles['mafia'], toscd.get_role(702607003121352725)],
            'ambusher': [base_roles['mafia'], toscd.get_role(702607082309812315)],
            'blackmailer': [base_roles['mafia'], toscd.get_role(702606728042250310)],
            'consigliere': [base_roles['mafia'], toscd.get_role(702606772950532096)],
            'consort': [base_roles['mafia'], toscd.get_role(702606817930510366)],
            'disguiser': [base_roles['mafia'], toscd.get_role(702606851208118322)],
            'forger': [base_roles['mafia'], toscd.get_role(702607929593036862)],
            'framer': [base_roles['mafia'], toscd.get_role(702606878613438474)],
            'janitor': [base_roles['mafia'], toscd.get_role(702606960456892426)],
            'hypnotist': [base_roles['mafia'], toscd.get_role(702607035400716338)],

            'arsonist': [base_roles['neutral_killing'], toscd.get_role(702609500011757598)],
            'serialkiller': [base_roles['neutral_killing'], toscd.get_role(702609585458118777)],
            'werewolf': [base_roles['neutral_killing'], toscd.get_role(702609629795844227)],
            'juggernaut': [base_roles['neutral_killing'], toscd.get_role(702609540881055904)],

            'executioner': [base_roles['neutral_evil'], toscd.get_role(702609404331294953)],
            'jester': [base_roles['neutral_evil'], toscd.get_role(702609442696331290)],
            'witch': [base_roles['neutral_evil'], toscd.get_role(702609468567060521)],

            'amnesiac': [base_roles['neutral_benign'], toscd.get_role(702609003620073574)],
            'survivor': [base_roles['neutral_benign'], toscd.get_role(702609091121512508)],
            'guardianangel': [base_roles['neutral_benign'], toscd.get_role(702609047207280660)],

            'vampire': [base_roles['neutral_chaos'], toscd.get_role(702609358718107799)],
            'pirate': [base_roles['neutral_chaos'], toscd.get_role(702609138500239400)],
            'plaguebearer': [base_roles['neutral_chaos'], toscd.get_role(702609228099223642)],
            'pestilence': [base_roles['neutral_chaos'], toscd.get_role(702609295501426722)],
            'baker': [base_roles['neutral_chaos'], toscd.get_role(702619736277647542)],

            'covenleader': [base_roles['coven'], toscd.get_role(702608215388586085)],
            'hexmaster': [base_roles['coven'], toscd.get_role(702608250956415006)],
            'medusa': [base_roles['coven'], toscd.get_role(702608295722221669)],
            'necromancer': [base_roles['coven'], toscd.get_role(702608329658204190)],
            'poisoner': [base_roles['coven'], toscd.get_role(702608386675441724)],
            'potionmaster': [base_roles['coven'], toscd.get_role(702608428337594459)],
        }
        if ctx.channel.id not in [702600628601356362, 702602218095902872, 296069608216068098]:
            return await ctx.send(f'{ctx.author.mention} **||** This command is only usable in '
                                  '<#702600628601356362> or <#288463362357067777>.')
        elif newrole.lower() not in roles.keys():
            return await ctx.send(f'{ctx.author.mention} **||** For a list of roles, please check '
                                  '<#702602323310149643>.  Make sure capitalization is also followed.')

        for role in roles.values():
            if role[1].id in (crole.id for crole in ctx.author.roles):
                await ctx.author.remove_roles(*role, reason='Auto assigner (removal)')

        await ctx.author.add_roles(*roles[newrole.lower()], reason='Auto assigner')

        await ctx.send(f'{ctx.author.mention}, you have been assigned **{roles[newrole.lower()][1].name.title()}**')

    @commands.command()
    async def nsfw(self, ctx):
        """Gives you the NSFW role."""
        toscd = self.bot.get_guild(288455332173316106)
        nsfw = toscd.get_role(425123783863435276)
        if nsfw in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfw, reason='NSFW removal')
            await ctx.send(f"{ctx.author.mention}, you have been unassigned the NSFW role.")
            return
        else:
            await ctx.author.add_roles(nsfw, reason='NSFW addition')
            return await ctx.send(f"{ctx.author.mention}, you have been assigned the NSFW role.")
     
    @commands.command()
    async def lfg(self, ctx):
        """Gives you the LFG role."""
        toscd = self.bot.get_guild(288455332173316106)
        nsfw = toscd.get_role(633407913796567050)
        if nsfw in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfw, reason='LFG removal')
            await ctx.send(f"{ctx.author.mention}, you have been unassigned the LFG role.")
            return
        else:
            await ctx.author.add_roles(nsfw, reason='LFG addition')
            return await ctx.send(f"{ctx.author.mention}, you have been assigned the LFG role.") 
        
    @commands.command()
    async def gnotif(self, ctx):
        """Gives you the Game Notifications role."""
        toscd = self.bot.get_guild(288455332173316106)
        nsfw = toscd.get_role(379748801197637644)
        if nsfw in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfw, reason='gnotif removal')
            await ctx.send(f"{ctx.author.mention}, you have been unassigned the Game Notifications role.")
            return
        else:
            await ctx.author.add_roles(nsfw, reason='LFG addition')
            return await ctx.send(f"{ctx.author.mention}, you have been assigned the Game Notifications role.") 
        
    @commands.command()
    async def coven(self, ctx):
        """Gives you the Coven Notifications role."""
        toscd = self.bot.get_guild(288455332173316106)
        nsfw = toscd.get_role(358655924342095874)
        if nsfw in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfw, reason='cnotif removal')
            await ctx.send(f"{ctx.author.mention}, you have been unassigned the Coven Notifications role.")
            return
        else:
            await ctx.author.add_roles(nsfw, reason='cnotif addition')
            return await ctx.send(f"{ctx.author.mention}, you have been assigned the Coven Notifications role.") 


def setup(bot):
    n = SelfRoles(bot)
    bot.add_cog(n)
