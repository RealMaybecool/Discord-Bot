from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import discord
import settings


class Kick:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, member: discord.Member = None):
        await self.bot.send_message(member, settings.kick_direct)
        await self.bot.kick(member)
        await self.bot.say(settings.kick_message + member.mention + settings.kick_message2 + settings.name)

    @kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, CheckFailure):
            await self.bot.send_message(ctx.message.channel, settings.permission_error)


def setup(bot):
    bot.add_cog(Kick(bot))

class Ban:

    def _init_(self, bot):

    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True, kick_members=True)
      async def ban(self, ctx, member: discord.Member = none):
        await self.bot.send.messege(member, settings.ban_direct)
        await self.botban(member)
        await self.bot.say(settings.ban_message + member.mention + settings.ban_messege2 + settings.name)

@ban.error 
async def ban_error(self, error, ctx):
    if isinstance(error, CheckFailure):
        await self.bot.send_message(ctx.messege.channel, settings.permission_error)

    def setup(bot):
        bot.add_cog(Ban(bot))
            
