from pyrogram import filters
from pyrogram.types import ChatPermissions
from Vinci import arpi
import asyncio


#----------- BAN ---------------#
@arpi.on_message(filters.command("ban", ",") & filters.me)
async def ban(client, message):
    if message.reply_to_message.from_user:
        userid=message.reply_to_message.from_user.id 

    if len(message.command) > 1:
        if message.command[1].isdigit():
            userid=int(message.command[1])
        elif message.command[1].startswith("@"):
            userid=message.command[1]
        #Add Option to Send Different Message When An Admin tries To Ban Another Admin
        else:
            return await message.edit_text("`Special User!`")

    else:
        return await message.edit_text("`Special User!`")

    me=await client.get_me()
    try:
        user=await client.get_me(userid)
    except Exception as e:
        return await message.edit_text(f"{e}")

    if user.id == me.id:
        return await message.edit_text("`Are uh mad?\nU r trying to ban yourself")

    try:
        await message.chat.kick_member(user.id)
        await message.edit_text(f"Banned {user.mention}")
    except Exception as e:
        await message.edit_text(str(e))




#-------------UNBAN-------------------#

@arpi.on_message(filters.command("unban", ",") & filters.me)
async def unban(client, message):
    if message.reply_to_message.from_user:
        userid=message.reply_to_message.from_user.id 

    if len(message.command) > 1:
        if message.command[1].isdigit():
            userid=int(message.command[1])
        elif message.command[1].starwith("@"):
            userid=message.command[1]
        else:
            return await message.edit_text("`Special User!`")

    else:
        return await message.edit_text("`Special User!`")

    me=await client.get_me()
    try:
        user=await client.get_me(userid)
    except Exception as e:
        return await message.edit_text(f"{e}")

    if user.id == me.id:
        return await message.edit_text("`Are uh mad?\nU r trying to unban yourself")

    try:
        await message.chat.unban_member(user.id)
        await message.edit_text(f"UnBanned {user.mention}")
    except Exception as e:
        await message.edit_text(str(e))
    await asyncio.sleep(2)
    await message.delete()


#--------------KICK-----------------#

@arpi.on_message(filters.command("kick", ",") & filters.me)
async def kick(client, message):
    if message.reply_to_message.from_user:
        userid=message.reply_to_message.from_user.id 

    if len(message.command) > 1:
        if message.command[1].isdigit():
            userid=int(message.command[1])
        elif message.command[1].starwith("@"):
            userid=message.command[1]
        else:
            return await message.edit_text("`Special User!`")

    else:
        return await message.edit_text("`Special User!`")

    me=await client.get_me()
    try:
        user=await client.get_me(userid)
    except Exception as e:
        return await message.edit_text(f"{e}")

    if user.id == me.id:
        return await message.edit_text("`Are uh mad?\nU r trying to kick yourself")

    try:
        await message.chat.kick_member(user.id)
        await message.chat.unban_member(user.id)
        await message.edit_text(f"Kicked {user.mention}")
    except Exception as e:
        await message.edit_text(str(e))
    await asyncio.sleep(2)
    await message.delete()



#-------------MUTE-------------------#

@arpi.on_message(filters.command("mute", ",") & filters.me)
async def mute(client, message):
    if message. reply_to_message.from_user:
        userid=message.reply_to_message.from_user.id 

    if len(message.command) > 1:
        if message.command[1].isdigit():
            userid=int(message.command[1])
        elif message.command[1].starwith("@"):
            userid=message.command[1]
        else:
            return await message.edit_text("`Special User!`")

    else:
        return await message.edit_text("`Special User!`")

    me=await client.get_me()
    try:
        user=await client.get_me(userid)
    except Exception as e:
        return await message.edit_text(f"{e}")

    if user.id == me.id:
        return await message.edit_text("`Are uh mad?\nU r trying to mute yourself")

    try:
        await message.chat.restrict_member(user.id, ChatPermissions())
        await message.edit_text(f"Muted {user.mention}")
    except Exception as e:
        await message.edit_text(f"{e}")
    await asyncio.sleep(2)
    await message.delete()

#--------------UNMUTE----------------------#

@arpi.on_message(filters.command("unmute", ",") & filters.me)
async def unmute(client, message):
    if message. reply_to_message.from_user:
        userid=message.reply_to_message.from_user.id 

    if len(message.command) > 1:
        if message.command[1].isdigit():
            userid=int(message.command[1])
        elif message.command[1].starwith("@"):
            userid=message.command[1]
        else:
            return await message.edit_text("`Special User!`")

    else:
        return await message.edit_text("`Special User!`")

    me=await client.get_me()
    try:
        user=await client.get_me(userid)
    except Exception as e:
        return await message.edit_text(f"{e}")

    if user.id == me.id:
        return await message.edit_text("`Are uh mad?\nU r trying to unmute yourself")

    try:
        await message.chat.unban_member(user.id)
        await message.edit_text(f"UnMuted {user.mention}")
    except Exception as e:
        await message.edit_text(str(e))
    await asyncio.sleep(2)
    await message.delete()


#-----------------PIN & UNPIN------------------------#

@arpi.on_message(filters.command("pin", ",") & filters.me)
async def pin(client, message):
    if not message.reply_to_message:
        return await message.edit_text("`uff! uh fool. Reply to any message to pin")

    try:
        await message.reply_to_message.pin()
        await message.edit_text("Pinned!")
    except Exception as e:
        await message.edit_text(str(e))
    await asyncio.sleep(2)
    await message.delete()

@arpi.on_message(filters.command("unpin", ",") & filters.me)
async def unpin(client, message):
    if not message.reply_to_message:
        return await message.edit_text("`uff! uh fool. Reply to any message to pin")

    try:
        await message.reply_to_message.pin()
        await message.edit_text("UnPinned!")
    except Exception as e:
        await message.edit_text(str(e))
    await asyncio.sleep(2)
    await message.delete()

#----------------PROMOTE & DEMOTE -----------------#

@arpi.on_message(filters.command("promote", ",") & filters.me)
async def promote(client, message):
    try:
        title = "Admin"
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
            title = str(get_arg(message))
        else:
            args = get_args(message)
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
        get_user = await app.get_users(user)
        await app.promote_chat_member(message.chat.id, user, can_manage_chat=True, can_change_info=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True, can_manage_voice_chats=True)
        await message.edit(
            f"Successfully Promoted [{get_user.first_name}](tg://user?id={get_user.id}) with title {title}"
        )

    except Exception as e:
        await message.edit(f"{e}")

    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass

@arpi.on_message(filters.command("demote", ",") & filters.me)
async def demote(client, message):
    try:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
        get_user = await app.get_users(user)
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(
            f"Successfully Demoted [{get_user.first_name}](tg://user?id={get_user.id})"
        )
    except Exception as e:
        await message.edit(f"{e}")

   
