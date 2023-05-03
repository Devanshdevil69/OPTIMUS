from OPTIMUS import amaan, HANDLER, SUDO_USERS
from datetime import datetime
from pyrogram import filters



@amaan.on_message(filters.command("stats", HANDLER) & filters.me)
@amaan.on_message(filters.command("stats", HANDLER) & filters.user(SUDO_USERS))
async def stats(client, message):
    await message.edit_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    group = ["supergroup", "group"]
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
        if user_s.status in ("creator", "administrator"):
            a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1
            
    end = datetime.now()
    ms = (end - start).seconds
    await message.edit_text(
        """`⚡️ Your Stats Obtained in {} seconds ⚡️`
`💫 You have {} Private Messages 💫`
`✨ You are in {} Groups ✨`
`🔥 You are in {} Super Groups 🔥`
`⭐️ You Are in {} Channels ⭐️`
`🌟 You Are Admin in {} Chats 🌟`
`❇️ Bots = {} ❇️`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )
