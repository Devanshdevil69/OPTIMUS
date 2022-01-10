from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
async def seddis(client, message):
  if not message.reply_to_message:
    return await message.reply_to_message.edit('Reply to a self distructing media !.!.!')
  k = await client.get_message.reply_to_message
  pic = await k.download_media()
  await client.send_media(chat_id, pic)
  await message.delete()
