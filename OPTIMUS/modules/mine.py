#For My own channel

from OPTIMUS import amaan
from pyrogram import filters


@amaan.on_message(filters.chat(-1001713433328) & filters.web_page)
def off_web(client, message):
    message.edit_text(message.text, disable_web_page_preview=True)


@amaan.on_message(filters.chat(-1001713433328) & filters.forwarded)
def del_forwarded(client, message):
    message.delete()
