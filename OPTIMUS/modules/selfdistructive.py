from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
async def seddis(client, message):
  if not message.reply_to_message:
    return await message.edit_text('Reply to a self distructing media !.!.!')
    k = await.message.reply_to_message
    pic = await message.download()
    message.delete()
  await client.send_message("me", pic)
