import traceback
import textwrap
from contextlib import redirect_stdout
import io
from platform import python_version
import copy

import discord
from discord.ext import commands

# Meta = things being done to the bot itself


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    @staticmethod
    def cleanup_code(content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')

    @commands.command(hidden=True, name='eval', aliases=['evaluate'])
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        # Evaluates a piece of code
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        # iOS Form
        body = body.replace("“", '"')
        body = body.replace("”", '"')
        body = body.replace("‘", "'")
        body = body.replace("’", "'")

        icon = "http://i.imgur.com/9EftiVK.png"

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as exc:
            fooem = discord.Embed(color=0xff0000)
            fooem.add_field(name="Code evaluation was not successful. <a:warped:724630886317817927>", value=f'```\n{exc.__class__.__name__}: {exc}\n```'
                            .replace(self.bot.http.token, '•' * len(self.bot.http.token)))
            fooem.set_footer(
                text=f"Evaluated using Python {python_version()}", icon_url=icon)
            fooem.timestamp = ctx.message.created_at
            return await ctx.send(embed=fooem)

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as exc:
            value = stdout.getvalue()
            fooem = discord.Embed(color=0xff0000)
            fooem.add_field(name="Code evaluation was not successful. <a:warped:724630886317817927>", value=f'```py\n{value}{traceback.format_exc()}'
                            f'\n```'.replace(self.bot.http.token,
                                             '•' * len(self.bot.http.token)))
            fooem.set_footer(
                text=f"Evaluated using Python {python_version()}", icon_url=icon)
            fooem.timestamp = ctx.message.created_at
            await ctx.send(embed=fooem)
        else:
            value = stdout.getvalue()

            try:
                await ctx.message.add_reaction(':white_check_mark:')
            except:
                pass

            if ret is None:
                if value:
                    sfooem = discord.Embed(color=discord.Colour.green())
                    sfooem.add_field(name="Code evaluation was successful! <a:WumpusHype:724630580687405056>", value=f'```py\n{value}\n```'.
                                     replace(self.bot.http.token, '•' * len(self.bot.http.token)))
                    sfooem.set_footer(
                        text=f"Evaluated using Python {python_version()}", icon_url=icon)
                    sfooem.timestamp = ctx.message.created_at
                    await ctx.send(embed=sfooem)
            else:
                self._last_result = ret
                ssfooem = discord.Embed(color=discord.Colour.green())
                ssfooem.add_field(name="Code evaluation was successful! <a:WumpusHype:724630580687405056>", value=f'```py\n{value}{ret}\n```'
                                  .replace(self.bot.http.token, '•' * len(self.bot.http.token)))
                ssfooem.set_footer(
                    text=f"Evaluated using Python {python_version()}", icon_url=icon)
                ssfooem.timestamp = ctx.message.created_at
                await ctx.send(embed=ssfooem)

    @commands.command(name="echo", hidden=True, aliases=["say", "print"])
    @commands.is_owner()
    async def echo(self, ctx, *, content):
        await ctx.send(content)

    @commands.command(name="runas", hidden=True, aliases=["impersonate"])
    @commands.is_owner()
    async def runas(self, ctx, member: discord.Member, *, cmd):
        # Invoke bot command as specified user.
        msg = copy.copy(ctx.message)
        msg.content = f"{ctx.me.mention} {cmd}"
        msg.author = member
        await self.bot.process_commands(msg)

    @commands.command(name="restart", aliases=["reboot"], hidden=True)
    @commands.is_owner()
    async def restart(self, ctx):
        # Restarts the bot
        await ctx.send("Restarting...")
        await self.bot.logout()
        raise KeyboardInterrupt


def setup(bot):
    bot.add_cog(Owner(bot))
