from discord.ext import commands

from modules import bot_ext


be = bot_ext.BotExt()


HELPS = {
    "help": ["ヘルプを表示", "コマンドヘルプを表示します。\ncommand引数にコマンド名を指定すると指定したコマンドの詳細が表示されます。", "[command: string]"]
}


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):
        await ctx.send(embed=be.embed(["test", "desc"]))


def setup(bot):
    bot.add_cog(CommandCog(bot))
