# ported from telebot
# i ported from shivam's project :) 
# rewritten in pyro by @CRiMiNaL786 

import os
from pyrogram import filters
from pyrogram.types import Chat
from OPTIMUS import amaan, HANDLER, SUDO_USERS

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**TO PM SOMEONE**
• `{HANDLER}pmto` <username> <message>
"""


@amaan.on_message(filters.command("pmto", HANDLER) & filters.me)
@amaan.on_message(filters.command("pmto", HANDLER) & filters.user(SUDO_USERS))
async def pmto(client, message):
    a = message.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await client.send_message(chat_id, msg)
        await message.edit_text("Message sent!")
    except BaseException:
        await message.edit_text("Something went wrong.")
