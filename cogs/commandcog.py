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
    @commands.command(name="test")
    async def b_o_t_(self, ctx):
        await ctx.send(embed=be.embed(["概要", "test"], thumbnail=self.bot.user.avatar_url, author=["botの情報", {
            "url": os.environ["DISCORD_BOT_INVITE"],
            "icon": "https://f.easyuploader.app/eu-prd/upload/20200921165534_6739487862584363444f.png"
        }], fields=[
            ["名前", self.bot.user.name, True],
            ["ID", self.bot.user.name, True],
            [None, None, True],
            ["サーバー数", f"{len(self.bot.guilds)} servers", True],
            ["メンバー数", f"{sum([g.member_count for g in self.bot.guilds])} members", True],
            [None, None, True],
            ["開発者", self.bot.get_user(self.bot.owner_id).name, True],
            ["開発言語", "Python", True],
            ["作成日時", "{0:%Y-%m-%d %H:%M:%S}".format(self.bot.user.created_at), True]
        ]))
    """@commands.group(name="bot")
    async def b_o_t_(self, ctx):
        if ctx.invoked_subcommand is None: await ctx.send(embed=be.embed(["botの情報", None], fields=[
            ["名前", self.bot.user.name, True],
            ["ID", self.bot.user.id, True],
            [None, None, True],
            ["サーバー数", f"{len(self.bot.guilds)} servers", True],
            ["メンバー数", f"{sum([g.member_count for g in self.bot.guilds])} members", True],
            [None, None, True],
            ["作成日時", "{0:%Y-%m-%d %H:%M:%S}".format(self.bot.user.created_at), True]
        ]))

    @b_o_t_.command()
    async def invite(self, ctx):
        await ctx.send(embed=be.embed(["招待", f"[botを招待する]({os.environ['DISCORD_BOT_INVITE']})"]))"""
    #----------


def setup(bot):
    bot.add_cog(CommandCog(bot))
