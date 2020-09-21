import os

from discord.ext import commands

from modules import bot_ext


be = bot_ext.BotExt()


HELPS = {
    "help": ["ヘルプを表示", "コマンドヘルプを表示します。\ncommand引数にコマンド名を指定すると指定したコマンドの詳細が表示されます。", "[command: string]"]
}


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # help -----
    @commands.command(name="help")
    async def help_(self, ctx, *args):
        if len(args) > 0:
            if not args[0] in HELPS: return await ctx.send(embed=be.embed(["エラー", f'"{args[0]}"というコマンドは見つかりませんでした'], escape=True))
            await ctx.send(embed=be.embed([f"{args[0]} {HELPS[args[0]][2]}", HELPS[args[0]][1]]))

        else: await ctx.send(embed=be.embed(["コマンドヘルプ", f'**`プレフィックス: "{os.environ["DISCORD_BOT_PREFIX"]}"`**\n**`help {HELPS["help"][2]}`**で詳細なコマンドヘルプ'], fields=[[k, HELPS[k][0], True] for k in HELPS]))
    #-----------

    # bot -----
    @commands.command(name="bot")
    async def b_o_t_(self, ctx):
        await ctx.send("abc")
    #----------


def setup(bot):
    bot.add_cog(CommandCog(bot))
