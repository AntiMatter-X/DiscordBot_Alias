from discord.ext import commands

from modules import bot_ext


be = bot_ext.BotExt()


class SecretCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # pien -----
    @commands.command()
    async def pien(self, ctx):
        await ctx.message.add_reaction("\U0001F97A")
    #-----------


def setup(bot):
    bot.add_cog(SecretCommandCog(bot))
