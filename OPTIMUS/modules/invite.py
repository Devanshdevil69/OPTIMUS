from pyrogram import filters
from OPTIMUS import amaan, HANDLER, SUDO_USERS
import asyncio

@amaan.on_message(filters.command("invite", HANDLER) & filters.me)
@amaan.on_message(filters.command("invite", HANDLER) & filters.user(SUDO_USERS))
async def inviteee(client, message):
    mg = await message.edit_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ",1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")
