import os
import discord
import datetime

from discord.ext import commands


async def refresh_act(bot):
    await bot.change_presence(activity=discord.Game(name=" | ".join([
        f"{os.environ['DISCORD_BOT_PREFIX']}help",
        f"{len(bot.guilds)} servers",
        f"{sum([g.member_count for g in bot.guilds])} members",
        f"refresh date: {'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9), 'JST')))}"
    ])))


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): await refresh_act(self.bot)

    @commands.Cog.listener()
    async def on_guild_join(self, guild): await refresh_act(self.bot)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild): await refresh_act(self.bot)

    @commands.Cog.listener()
    async def on_member_join(self, member): await refresh_act(self.bot)

    @commands.Cog.listener
    async def on_member_remove(self, member): await refresh_act(self.bot)


def setup(bot):
    bot.add_cog(EventCog(bot))
