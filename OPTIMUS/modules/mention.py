from OPTIMUS import amaan, HANDLER, SUDO_USERS
from pyrogram import filters
import html
import os

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**UseR Mention AnD TaGALL**
• {HANDLER}mention <username without @> <custom text>
• {HANDLER}tagall 
"""
# mention user 

@amaan.on_message(filters.command("mention", HANDLER) & filters.me)
@amaan.on_message(filters.command("mention", HANDLER) & filters.user(SUDO_USERS))
async def mention(client, message):
    args = message.text.split(None, 2)
    if len(args) == 3:
        user = args[1]
        name = args[2]
        rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
        await message.edit_text(
            rep,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    else:
        await message.edit_text(f"Usage: `{HANDLER}mention (username without @) (custom text)`")
        return


# mention all AND his helper

def mention_html(user_id, name):
    return u'<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))


@amaan.on_message(filters.command("tagall", HANDLER) & filters.me)
@amaan.on_message(filters.command("tagall", HANDLER) & filters.user(SUDO_USERS))
async def tag_all_users(client, message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "Hi all 🙃"
    kek = client.iter_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id,
                                  parse_mode="html")
    else:
        await client.send_message(message.chat.id, text, parse_mode="html")

