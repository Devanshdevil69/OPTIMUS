import os
from OPTIMUS import amaan, HANDLER, SUDO_USERS
from pyrogram import filters

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**GET IDs**
• {HANDLER}id -tag any user or media

"""

@amaan.on_message(filters.command("id", HANDLER) & filters.me)
@amaan.on_message(filters.command("id", HANDLER) & filters.user(SUDO_USERS))
async def get_id(client, message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message
        if rep.audio:
            file_id = rep.audio.file_id
        elif rep.document:
            file_id = rep.document.file_id
        elif rep.photo:
            file_id = rep.photo.file_id
        elif rep.sticker:
            file_id = rep.sticker.file_id
        elif rep.video:
            file_id = rep.video.file_id
        elif rep.animation:
            file_id = rep.animation.file_id
        elif rep.voice:
            file_id = rep.voice.file_id
        elif rep.video_note:
            file_id = rep.video_note.file_id
        elif rep.contact:
            file_id = rep.contact.file_id
        elif rep.location:
            file_id = rep.location.file_id
        elif rep.venue:
            file_id = rep.venue.file_id
        elif rep.from_user:
            if rep.forward_from:
                user_id = rep.forward_from.id
                if rep.forward_from.last_name:
                    user_name = (
                        rep.forward_from.first_name + " " + rep.forward_from.last_name
                    )
                else:
                    user_name = rep.forward_from.first_name
                username = rep.forward_from.username
            else:
                user_id = rep.from_user.id
                if rep.from_user.last_name:
                    user_name = rep.from_user.first_name + " " + rep.from_user.last_name
                else:
                    user_name = rep.from_user.first_name
                username = rep.from_user.username

    if user_id:
        await message.edit_text(
            "**User ID:** `{}`\n**Name:** `{}`\n**Username:** @{}".format(
                user_id, user_name, username
            )
        )
    elif file_id:
        await message.edit_text(f"**File's ID:** `{file_id}`")
    else:
        await message.edit_text(f"**This Chat's ID:** `{m.chat.id}`")
