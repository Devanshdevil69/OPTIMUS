#For My own channel

from Vinci import arpi
from pyrogram import filters


@arpi.on_message(filters.chat(-1001713433328) & filters.web_page)
def off_web(client, message):
    message.edit_text(message.text, disable_web_page_preview=True)


@arpi.on_message(filters.chat(-1001713433328) & filters.forwarded)
def del_forwarded(client, message):
    message.delete()
