from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.raw.functions.channels import GetAdminedPublicChannels
from OPTIMUS import amaan, HANDLER
import asyncio



@amaan.on_message(filters.command("listmyusernames", HANDLER) & filters.me)
async def listmun(client, message):
    result = await client.send(GetAdminedPublicChannels())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await message.edit_text(output_str)
