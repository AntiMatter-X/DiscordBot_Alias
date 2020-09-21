import discord


_escape_md = lambda b, s: discord.utils.escape_markdown(s) if b else s


class BotExt:
    def __init__(self, color=0x5480f3):
        self.color = color

    # 渡されたデータを枠付きにして返す
    def border(self, data, **options):
        if type(data) is not list: return "ERROR"
        if "header" in options: header = options["header"] if any([
            all([options["header"], options["header"] is not True]),
            options["header"] is None,
            options["header"] is False
        ]) else ["name", "value"]
        else: header = None
        upper = options["upper"] if "upper" in options else False
        if header:
            data.insert(0, [header[0], header[1].upper() if upper else header[1]])
            data.insert(1, ["-" * len(max([str(v[0]) for v in data], key=len)), "-" * len(max([str(v[1]) for v in data], key=len))])
        names = [(str(v[0]).upper() if upper else str(v[0])) + " " * (len(max([str(v[0]) for v in data], key=len)) - len(str(v[0]))) for v in data]
        vals = [str(v[1]) + " " * (len(max([str(v[1]) for v in data], key=len)) - len(str(v[1]))) for v in data]
        infos = [f"+-{names[i]}-+-{vals[i]}-+" if header and i == 1 else f"| {names[i]} | {vals[i]} |" for i in range(len(names))]
        border = f"+{'-' * (len(names[0]) + 2)}+{'-' * (len(vals[0]) + 2)}+"
        return border + "\n" + "\n".join(infos) + "\n" + border

    # 埋め込みを作成するメソッド
    def embed(self, embed_data, **options):
        if any([type(embed_data) is not list, len(embed_data) < 2]): return "ERROR"
        embed = discord.Embed(
            title=_escape_md(options["escape"] if "escape" in options else False, embed_data[0]) if embed_data[0] else "\0",
            description=_escape_md(options["escape"] if "escape" in options else False, embed_data[1]) if embed_data[1] else "\0",
            url=options["url"] if "url" in options else None,
            color=options["color"] if "color" in options else self.color
        )
        if "author" in options:
            if type(options["author"]) is not list: return "ERROR"
            if len(options["author"]) == 0: return "ERROR"
            if len(options["author"]) < 2: options["author"].append({})
            embed.set_author(
                name=_escape_md(options["escape"] if "escape" in options else False, options["author"][0] if options["author"][0] else "\0"),
                url=options["author"][1]["url"] if "url" in options["author"][1] else None,
                icon=options["author"][1]["icon"] if "icon" in options["author"][1] else None,
            )
        if "fields" in options:
            if type(options["fields"]) is not list: return "ERROR"
            for f in options["fields"]:
                if any([type(f) is not list, len(f) < 2]): return "ERROR"
                if len(f) < 3: f.append(False)
                embed.add_field(
                    name=_escape_md(options["escape"] if "escape" in options else False, f[0]) if f[0] else "\0",
                    value=_escape_md(options["escape"] if "escape" in options else False, f[1]) if f[1] else "\0",
                    inline=f[2]
                )
        if "thumbnail" in options: embed.set_thumbnail(url=options["thumbnail"])
        if "image" in options: embed.set_image(url=options["image"])
        return embed
