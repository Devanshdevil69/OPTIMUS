#For My own channel

import os
from OPTIMUS import amaan
from pyrogram import filters


__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = """ DON'T KNOW """

@amaan.on_message(filters.chat(-1001616881967) & filters.web_page)
def off_web(client, message):
    message.edit_text(message.text, disable_web_page_preview=True)


@amaan.on_message(filters.chat(-1001616881967) & filters.forwarded)
def del_forwarded(client, message):
    message.delete()
