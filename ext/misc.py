import discord
from discord.ext import commands
import random
try:
    from config import lelijah
except ModuleNotFoundError:  # Travis CI check compat
    class config:
        lelijah = """                _,-----._____
                               _,-'      .:::.  `-._
                              /                     `-.
                             /                       .::.
                            /            ______       .::\
                        ___|        __.-'\ .::.`--._  .:::\
                 ___,--'   /     _,'    .:\  : /    `-.::::\
                /   `-.    |   .'       .::\  /       .`:::|
               _|      `.  | .'          .::)/         ::\:/
          _,--(`\        \ |/           .::/ ).       .:::V
         / .:._\_\.   ,--. (            .::| /.       .:::|
        /.:_,-'    \_|    \_|           .::|/.        .:::/
        \ <  | \      \   .:|           .::||.        .::/
        { <   \`  , /\ \   :\           .::|/.       .::/
        |  <_ , , ` \,-/\.   |         .:::/.       .:::/
        \  \:`+----'::/  `.  |        ..:::|.      .:::/
        | ..  `.:::::/     \_|        ..::|:.      .::/
         \ :.   <:::/        \        ..::|:.      .:/
          \_ .  <:/           |       ..::|.       ::/
            \__  /            |        .::|.      .:/
               `'             \         ::|.    .::/
                               \        ::|.   .::/
                               |       .::|.   .::/
                               |..  .  .:/:.  . :(
                               /    .:.:/::.   ..:\_
                              /     .:::X::.      .::.
                             /     .:::/ \_.        .:\
                            /       .:|    `.        .:\
                           |        .:|      \        .:\
                           |        .:|        \       .:\
                           |       .::|         \       .:\
                           |       .::/          \       .:|
                           |       .:/            \       .\
                            \      .:|              \      .\
                            |     .:/                \      .\
                            |     .:|                 \       \
                            |    .:/                   \      .\
                            |   .:/                     \      .\
                            |   .:|                      \.    .:\,
                            |   ::|                       \.   _//.`.
                            /  .::\                       |:._//   .:\
                           /  _.:::\                      L_' |    .:)
                           L='``:::/                      |  || ,-'.:|
                          //  .::\|                       \==\\/_   :|
                         /     .::|                      /|__///#\  :|
                         | _,-._ :/                     /\\__//###\ :|
                         \/   .://|                     \     /####\:|
                        /\\   :/,'|                      \___/#*`'  ||
                        |/#\  :|,'|
                        |/##\ :|\,/
                         /##| :|#\|
                         `**|_:|mthw """


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
