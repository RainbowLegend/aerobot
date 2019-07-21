import discord
from discord.ext import commands
import random
lelijah = """                                          _..  
                                                   .qd$$$$bp.
                                                 .q$$$$$$$$$$m.
                                                .$$$$$$$$$$$$$$
                                              .q$$$$$$$$$$$$$$$$
                                             .$$$$$$$$$$$$P\$$$$;
                                           .q$$$$$$$$$P^"_.`;$$$$
                                          q$$$$$$$P;\   ,  /$$$$P
                                        .$$$P^::Y$/`  _  .:.$$$/
                                       .P.:..    \ `._.-:.. \$P
                                       $':.  __.. :   :..    :'
                                      /:_..::.   `. .:.    .'|
                                    _::..          T:..   /  :
                                 .::..             J:..  :  :
                              .::..          7:..   F:.. :  ;
                          _.::..             |:..   J:.. `./
                     _..:::..               /J:..    F:.  : 
                   .::::..                .T  \:..   J:.  /
                  /:::...               .' `.  \:..   F_o'
                 .:::...              .'     \  \:..  J ;
                 ::::...           .-'`.    _.`._\:..  \'
                 ':::...         .'  `._7.-'_.-  `\:.   \
                  \:::...   _..-'__.._/_.--' ,:.   b:.   \._ 
                   `::::..-"_.'-"_..--"      :..   /):.   `.\   
                     `-:/"-7.--""            _::.-'P::..    \} 
          _....------""""""            _..--".-'   \::..     `. 
         (::..              _...----"""  _.-'       `---:..    `-.
          \::..      _.-""""   `""""---""                `::...___)
           `\:._.-"""                             """


class Misc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def penis(self, ctx, user: discord.Member=None):
        """:b:enis?"""
        if user.id == 555897749762080778:
            return await ctx.send(lelijah)
        elif user is None:
            user = ctx.author
        state = random.getstate()
        random.seed(user.id)
        random.setstate(state)
        await ctx.send(f"Size: 8{'=' * random.randint(0, 30)}D")


def setup(bot):
    bot.add_cog(Misc(bot))
