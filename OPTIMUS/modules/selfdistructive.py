import os
from pyrogram import filters
from OPTIMUS import amaan, HANDLER, SUDO_USERS


__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**DOWNLOADS THE SECRET MEDIA OR TIMER MEDIA AND SEND TO SAVED MESSAGES**
USAGE :- TAG THAT MEDIA AND SEND
{HANDLER}selfd

"""


@amaan.on_message(filters.command("selfd", HANDLER) & filters.me)
@amaan.on_message(filters.command("selfd", HANDLER) & filters.user(SUDO_USERS))
async def selfd(client, message):
  await message.delete()
  if not message.reply_to_message:
    return await message.edit_text('Reply to a self distructing media !.!.!')
  k = message.reply_to_message
  pic = await k.download()
  await client.send_document("me", pic)

