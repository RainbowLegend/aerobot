import discord
import json
from discord.ext import commands
from asyncio import TimeoutError as Timeout


def has_a_role():
    def predicate(ctx):
        with open('roles.json', 'r') as f:
            data = json.load(f)

        if str(ctx.author.id) in data:
            return True
        return False

    return commands.check(predicate)


def conv_hex(hex_val: str) -> int:
    hex_val = hex_val.split('#')[-1]
    return int(hex_val, base=16)


class CustomRoles:
    """"""
    def __init__(self, bot):
        self.bot = bot

        try:
            with open('roles.json', 'r') as f:
                json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            with open('roles.json', 'w+') as f:
                f.write("{}")

    @commands.command(name='CreateCustomRole', aliases=['ccr'])
    @commands.is_owner()
    async def create_custom_role(self, ctx, user: discord.Member):

        with open('roles.json', 'r') as f:
            data = json.load(f)

        if str(user.id) in data:
            return await ctx.send('That person already has a custom role!')

        r = await ctx.guild.create_role(reason='/ccr - new role', name=f"{user.id}'s role")

        data[str(user.id)] = r.id
        with open('roles.json', 'w') as f:
            json.dump(data, f)

        await user.add_roles(r, reason='/ccr - new role')

        try:
            await user.send('__Congrats on your new role! You have the available commands:__\n\n'
                            '`/rc` - Change your role colour. Needs to be in `#FFFFFF` or `FFFFFF` format.\n'
                            '`/rn` - Change your role name.\n'
                            '`/tr` - Transfer your role to someone else. This is irreversible.')
        except discord.HTTPException:
            pass

        return await ctx.send(f'Role `{r.name}` with repr `{repr(r)}` created.')

    @commands.command(name='rolecolour', aliases=['rolecolor', 'rc'])
    @has_a_role()
    async def change_role_color(self, ctx, hex_):

        with open('roles.json', 'r') as f:
            data = json.load(f)
            
        hex_ = conv_hex(hex_)

        role = ctx.guild.get_role(data[str(ctx.author.id)])

        await role.edit(
            reason=f'/rc - {role.id}',
            colour=discord.Colour(hex_),
            name=role.name,
            mentionable=False,
            hoisted=True,
            position=role.position,
            permissions=role.permissions
        )
        return await ctx.send('Role colour changed successfully.')

    @commands.command(name='rolename', aliases=['rn'])
    @has_a_role()
    async def change_role_name(self, ctx, *, name):

        with open('roles.json', 'r') as f:
            data = json.load(f)

        role = ctx.guild.get_role(data[str(ctx.author.id)])

        await role.edit(
            reason=f'/rc - {role.id}',
            colour=role.colour,
            name=name,
            mentionable=False,
            hoisted=True,
            position=role.position,
            permissions=role.permissions
        )

        return await ctx.send('Role name changed successfully.')

    @commands.command(name='transferrole', aliases=['tr'])
    @has_a_role()
    async def transfer_role(self, ctx, *, new_person: discord.Member):
        await ctx.send('Are you sure you want to transfer your custom role? This is irreversible. `Y/n`')
        try:
            await self.bot.wait_for(
                'message',
                timeout=15,
                check=lambda m: m.author.id == ctx.author.id and "y" in m.content.lower()
            )

            with open('roles.json', 'r') as f:
                data = json.load(f)

            role = ctx.guild.get_role(data[str(ctx.author.id)])

            await new_person.add_roles(role, reason='/tr request')
            await ctx.author.remove_roles(role, reason='/tr request')

            del data[str(ctx.author.id)]
            data[str(new_person.id)] = role

            with open('roles.json', 'w') as f:
                json.dump(data, f)

            return await ctx.send('Role successfully transferred.')

        except Timeout:
            await ctx.send('Timed out.')


def setup(bot: commands.Bot):
    c = CustomRoles(bot)
    bot.add_cog(c)
