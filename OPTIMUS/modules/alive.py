from Vinci import arpi
from pyrogram import filters, __version__
from sys import version_info




@arpi.on_message(filters.command("ping", ",") & filters.me)
async def ping(client, message):
    await message.edit_text("🏓Pong!")



@arpi.on_message(filters.command("alive", ",") & filters.me)
async def alive(client, message):
    text="**VINCI USERBOT**\n"
    text += f"\nPython Version: `{version_info[0]}.{version_info[1]}.{version_info[2]}`"
    text += f"\nPyrogram Version: {__version__}"

    await message.edit_text(text)

    
