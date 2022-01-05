from OPTIMUS import amaan, HANDLER
from pyrogram import filters

@amaan.on_message(filters.command("mention", HANDLER) & filters.me)
async def mention(client, message):
    args = message.text.split(None, 2)
    if len(args) == 3:
        user = args[1]
        name = args[2]
        rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
        await message.edit_text(
            rep,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    else:
        await message.edit_text(f"Usage: `{HANDLER}mention (username without @) (custom text)`")
        return
