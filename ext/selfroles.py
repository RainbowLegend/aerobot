from discord.ext import commands


class SelfRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tosrole", aliases=["role"])
    async def tosrole(self, ctx, *, newrole):

        toscd = self.bot.get_guild(702600628601356359)

        ALIGNMENT = {
            'town': toscd.get_role(702604255269355610),
            'mafia': toscd.get_role(702604336248913940),
            'neutral_killing': toscd.get_role(702604410215333978),
            'neutral_benign': toscd.get_role(702608855661543544),
            'neutral_evil': toscd.get_role(702609935669919875),
            'neutral_chaos': toscd.get_role(702604536208031806),
            'coven': toscd.get_role(702604367802400838)
        }

        roles = {
            'jailor': [ALIGNMENT['town'], toscd.get_role(702605931971608596)],
            'veteran': [ALIGNMENT['town'], toscd.get_role(702606280837300265)],
            'vigilante': [ALIGNMENT['town'], toscd.get_role(702606235588886549)],
            'vampirehunter': [ALIGNMENT['town'], toscd.get_role(702606377327132703)],
            'investigator': [ALIGNMENT['town'], toscd.get_role(702605669513298022)],
            'lookout': [ALIGNMENT['town'], toscd.get_role(702605806658519070)],
            'sheriff': [ALIGNMENT['town'], toscd.get_role(702605770721853442)],
            'spy': [ALIGNMENT['town'], toscd.get_role(702606204261892146)],
            'psychic': [ALIGNMENT['town'], toscd.get_role(702607505339056169)],
            'tracker': [ALIGNMENT['town'], toscd.get_role(702607562662609057)],
            'escort': [ALIGNMENT['town'], toscd.get_role(702605954050424994)],
            'mayor': [ALIGNMENT['town'], toscd.get_role(702606063446393004)],
            'medium': [ALIGNMENT['town'], toscd.get_role(702606095583150163)],
            'retributionist': [ALIGNMENT['town'], toscd.get_role(702606144241270897)],
            'transporter': [ALIGNMENT['town'], toscd.get_role(702606313430974575)],
            'doctor': [ALIGNMENT['town'], toscd.get_role(702605844747124856)],
            'bodyguard': [ALIGNMENT['town'], toscd.get_role(702605897926443118)],
            'crusader': [ALIGNMENT['town'], toscd.get_role(702607601308925995)],
            'trapper': [ALIGNMENT['town'], toscd.get_role(702607654224134154)],

            'godfather': [ALIGNMENT['mafia'], toscd.get_role(702606921630482492)],
            'mafioso': [ALIGNMENT['mafia'], toscd.get_role(702607003121352725)],
            'ambusher': [ALIGNMENT['mafia'], toscd.get_role(702607082309812315)],
            'blackmailer': [ALIGNMENT['mafia'], toscd.get_role(702606728042250310)],
            'consigliere': [ALIGNMENT['mafia'], toscd.get_role(702606772950532096)],
            'consort': [ALIGNMENT['mafia'], toscd.get_role(702606817930510366)],
            'disguiser': [ALIGNMENT['mafia'], toscd.get_role(702606851208118322)],
            'forger': [ALIGNMENT['mafia'], toscd.get_role(702607929593036862)],
            'framer': [ALIGNMENT['mafia'], toscd.get_role(702606878613438474)],
            'janitor': [ALIGNMENT['mafia'], toscd.get_role(702606960456892426)],
            'hypnotist': [ALIGNMENT['mafia'], toscd.get_role(702607035400716338)],

            'arsonist': [ALIGNMENT['neutral_killing'], toscd.get_role(702609500011757598)],
            'serialkiller': [ALIGNMENT['neutral_killing'], toscd.get_role(702609585458118777)],
            'werewolf': [ALIGNMENT['neutral_killing'], toscd.get_role(702609629795844227)],
            'juggernaut': [ALIGNMENT['neutral_killing'], toscd.get_role(702609540881055904)],

            'executioner': [ALIGNMENT['neutral_evil'], toscd.get_role(702609404331294953)],
            'jester': [ALIGNMENT['neutral_evil'], toscd.get_role(702609442696331290)],
            'witch': [ALIGNMENT['neutral_evil'], toscd.get_role(702609468567060521)],

            'amnesiac': [ALIGNMENT['neutral_benign'], toscd.get_role(702609003620073574)],
            'survivor': [ALIGNMENT['neutral_benign'], toscd.get_role(702609091121512508)],
            'guardianangel': [ALIGNMENT['neutral_benign'], toscd.get_role(702609047207280660)],

            'vampire': [ALIGNMENT['neutral_chaos'], toscd.get_role(702609358718107799)],
            'pirate': [ALIGNMENT['neutral_chaos'], toscd.get_role(702609138500239400)],
            'plaguebearer': [ALIGNMENT['neutral_chaos'], toscd.get_role(702609228099223642)],
            'pestilence': [ALIGNMENT['neutral_chaos'], toscd.get_role(702609295501426722)],
            'baker': [ALIGNMENT['neutral_chaos'], toscd.get_role(702619736277647542)],

            'covenleader': [ALIGNMENT['coven'], toscd.get_role(702608215388586085)],
            'hexmaster': [ALIGNMENT['coven'], toscd.get_role(702608250956415006)],
            'medusa': [ALIGNMENT['coven'], toscd.get_role(702608295722221669)],
            'necromancer': [ALIGNMENT['coven'], toscd.get_role(702608329658204190)],
            'poisoner': [ALIGNMENT['coven'], toscd.get_role(702608386675441724)],
            'potionmaster': [ALIGNMENT['coven'], toscd.get_role(702608428337594459)],
        }

        if ctx.channel.id not in [702603189324873768, 748238536636891217, 702602015896895590]:
            return await ctx.send(
                f'{ctx.author.mention} **||** Cette commande n\'est utilisable qu\'en  <#702603189324873768> et <#748238536636891217>')
        elif newrole.lower() not in roles.keys():
            return await ctx.send(
                f'{ctx.author.mention} **||** Pour une liste des rôles, veuillez vérifier <#702602323310149643>.  Assurez-vous que la capitalisation est également respectée.')

        for role in roles.values():
            if role[1].id in (crole.id for crole in ctx.author.roles):
                await ctx.author.remove_roles(*role, reason='Selfrole assigner (tos, removal)')

        await ctx.author.add_roles(*roles[newrole.lower()], reason='Selfrole assigner (tos, addition)')

        await ctx.send(f'{ctx.author.mention}, on vous a attribué **{roles[newrole.lower()][1].name.title()}**')

    @commands.command(name="nsfw", hidden=True, enabled=False)
    async def nsfw(self, ctx):
        """Gives you the NSFW role."""
        toscd = self.bot.get_guild(702600628601356359)
        nsfwRole = toscd.get_role(425123783863435276)
        if nsfwRole in ctx.message.author.roles:
            await ctx.author.remove_roles(nsfwRole, reason='Selfrole assigner (nsfw, removal)')
            await ctx.send(f"{ctx.author.mention}, le rôle NSFW vous a été annulé.")
            return
        else:
            await ctx.author.add_roles(nsfwRole, reason='Selfrole assigner (nsfw, addition)')
            return await ctx.send(f"{ctx.author.mention}, le rôle NSFW vous a été attribué.")

    @commands.command(name="lfg", aliases=["lookingforgames"], hidden=True, enabled=False)
    async def lfg(self, ctx):
        """Gives you the LFG role."""
        toscd = self.bot.get_guild(702600628601356359)
        lfgRole = toscd.get_role(633407913796567050)
        if lfgRole in ctx.message.author.roles:
            await ctx.author.remove_roles(lfgRole, reason='Selfrole assigner (lfg, removal)')
            await ctx.send(f"{ctx.author.mention}, le rôle LFG vous a été annulé.")
            return
        else:
            await ctx.author.add_roles(lfgRole, reason='Selfrole assigner (lfg, addition)')
            return await ctx.send(f"{ctx.author.mention}, le rôle LFG vous a été attribué.")

    @commands.command(name="gnotif", aliases=["gamenightnotify", "gamenightnotifications", "gamenightnotif"],
                      hidden=True, enabled=False)
    async def gnotif(self, ctx):
        toscd = self.bot.get_guild(702600628601356359)
        gnotif_role = toscd.get_role(379748801197637644)
        if gnotif_role in ctx.message.author.roles:
            await ctx.author.remove_roles(gnotif_role, reason='Selfrole assigner (gamenight notifications, removal)')
            await ctx.send(f"{ctx.author.mention}, vous n'avez plus attribué le rôle de notifications de jeu.")
            return
        else:
            await ctx.author.add_roles(gnotif_role, reason='Selfrole assigner (gamenight notifications, addition')
            return await ctx.send(f"{ctx.author.mention}, le rôle de notifications de jeu vous a été attribué.")

    @commands.command(name="cnotif", aliases=["covennotify", "covennotifications", "covennotif"], hidden=True,
                      enabled=False)
    async def cnotif(self, ctx):
        toscd = self.bot.get_guild(702600628601356359)
        cnotif_role = toscd.get_role(358655924342095874)
        if cnotif_role in ctx.message.author.roles:
            await ctx.author.remove_roles(cnotif_role, reason='Selfrole assinger (coven notifications, removal')
            await ctx.send(f"{ctx.author.mention}, vous n'avez plus été affecté au rôle Notifications Coven.")
            return
        else:
            await ctx.author.add_roles(cnotif_role, reason='Selfrole assigner (coven notifications, addition)')
            return await ctx.send(f"{ctx.author.mention}, vous avez reçu le rôle Notifications Coven.")


def setup(bot):
    bot.add_cog(SelfRoles(bot))
