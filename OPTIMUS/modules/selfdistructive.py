from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
async def selfd(client, message):
  await message.delete()
  if not message.reply_to_message:
    return await message.edit_text('Reply to a self distructing media !.!.!')
  k = message.reply_to_message
  pic = await k.download()
  await client.send_document("me", pic)
