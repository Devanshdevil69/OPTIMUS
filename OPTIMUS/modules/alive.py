from OPTIMUS import amaan, HANDLER, StartTime, ALIVE_PIC ,SUDO_USERS
from pyrogram import filters, __version__
from sys import version_info
from datetime import datetime
import asyncio
import time
import os

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = """
**ALIVE AND PING**
USAGE :-
• {HANDLER}alive

• {HANDLER}ping
"""
#ping

@amaan.on_message(filters.command("ping", HANDLER) & filters.me)
@amaan.on_message(filters.command("ping", HANDLER) & filters.user(SUDO_USERS))
async def ping(client, message):
    start = datetime.now()
    await message.edit_text("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000 
    await message.edit_text(f"**🏓PoNG!**\n`{m_s} ms`")

#alive

@amaan.on_message(filters.command("alive", HANDLER) & filters.me)
@amaan.on_message(filters.command("alive", HANDLER) & filters.user(SUDO_USERS))
async def alive(client, message):
    await message.delete()
    text="**OPTIMUS USERBOT**\n"
    text += f"\nPython Version: `{version_info[0]}.{version_info[1]}.{version_info[2]}`"
    text += f"\nPyrogram Version: `{__version__}`"
    text += f"\nCurrent Uptime: `{str(datetime.now() - StartTime).split('.')[0]}`"

    await client.send_photo(message.chat.id, ALIVE_PIC, caption=text)
if Exception:
             try:
                 await client.send_video(message.chat.id, ALIVE_PIC, caption=text)
