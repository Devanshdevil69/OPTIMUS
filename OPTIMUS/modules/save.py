from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("save", HANDLER) & filters.me)
async def to_saved(client, message):
    await message.reply_to_message.forward("self")
    await message.edit_text('`Message Has BeeN SaveD.`')
