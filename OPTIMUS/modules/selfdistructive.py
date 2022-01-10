from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
async def seddis(client, message):
  if not message.reply_to_message:
    return await message.edit_text('Reply to a self distructing media !.!.!')
  k = message.reply_to_message
  pic = await k.download()
  await client.send_message("chat_id, me", "pic")
