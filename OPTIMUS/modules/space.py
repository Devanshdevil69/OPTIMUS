from pyrogram import filters
from OPTIMUS import amaan, HANDLER

# S P A C E

@amaan.on_message(filters.command("space", HANDLER) & filters.me)
async def space(client, message):
    await message.edit_text("ㅤ")

# B L A N K

@amaan.on_message(filters.command("blank", HANDLER) & filters.me)
async def blank(client, message):
    await message.edit_text("­")
