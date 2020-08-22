from discord.ext import commands


class NitroPerks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild = bot.get_guild(702600628601356359)

    @commands.command(name="customrole")
    @commands.has_any_role(702614991446081578, 718662691861823489)
    async def roles(self, ctx, action, *, args):
        if action == "create":
            newrole = await self.guild.create_role(name=ctx.author.id, reason=f"Nitro Booster Role for {ctx.author.id}")
            ghost = self.guild.get_role(702605281204502638)
            current_guild_roles = self.guild.roles
            await newrole.edit(position=current_guild_roles.index(ghost) + 1)
            return await ctx.send("Your new role has been created!")
        if action == "color":
            userrole = discord.utils.get(self.guild.roles, name=ctx.author.id)
            if not userrole:
                return await ctx.send("Create a role first using `/customrole create`.")
            try:
                await userrole.edit(color=int(f"0x{args.strip('`')}"))
                return await ctx.send(f"You have changed your role's color to {args}!")
            except ValueError:
                return await ctx.send("Input a valid hex code such as `FFFFFF`!")
                

def setup(bot):
    bot.add_cog(NitroPerks(bot))
