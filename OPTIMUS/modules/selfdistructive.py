from pyrogram import filters
from OPTIMUS import amaan, HANDLER

@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
async def seddis(client, message):
  if not message.reply_to_message:
    return await message.edit_text('Reply to a self distructing media !.!.!')
  await message.delete()
  download_location = await client.download_media(message=message.reply_to_message,file_name='root/OPTIMUS/')
  pic = await message.download()
  await client.send_message("me", pic)
