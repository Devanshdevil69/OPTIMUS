from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.raw.functions.channels import GetAdminedPublicChannels
from OPTIMUS import amaan, HANDLER, SUDO_USERS
import asyncio
import os 

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**GET YOUR USERNAMES**
USAGE :- {HANDLER}listmyusernames
"""


@amaan.on_message(filters.command("listmyusernames", HANDLER) & filters.me)
@amaan.on_message(filters.command("listmyusernames", HANDLER) & filters.user(SUDO_USERS))
async def listmun(client, message):
    result = await client.invoke(GetAdminedPublicChannels())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await message.edit_text(output_str)

