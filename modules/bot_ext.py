import discord


_escape_md = lambda b, s: discord.utils.escape_markdown(s) if b else s


class BotExt:
