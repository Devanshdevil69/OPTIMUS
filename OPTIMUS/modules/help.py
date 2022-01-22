import os
from pyrogram import filters
from OPTIMUS import amaan, HANDLER
from OPTIMUS.modules import ALL_PLUGINS
from OPTIMUS import HELP_COMMANDS

HELP_DEFAULT = f"""
To get help for any command, just type `{HANDLER}help` plugin name
'PLUGiN NAME' should be the name of a proper plugin!

**Get a list of all Plugins using:**
`{HANDLER}plugins`
"""


@amaan.on_message(filters.command("plugins", HANDLER) & filters.me)
async def list_plugins(client, message):
    # Some Variables
    mods = ""
    mod_num = 0
    # Some Variables
    modules = list(HELP_COMMANDS.keys())
    for plug in modules:
        mods += f"`{plug}`\n"
        mod_num += 1
    all_plugins = f"<b><u>{mod_num}</u> Modules Currently Loaded:</b>\n\n" + mods
    await message.edit_text(all_plugins)
    return


@amaan.on_message(filters.command("help", HANDLER) & filters.me)
async def help_me(client, message):
    if len(message.command) == 1:
        await message.edit_text(HELP_DEFAULT)
    elif len(message.command) == 2:
        module_name = message.text.split(None, 1)[1]
        try:
            HELP = f"**Help for __{module_name}__**\n\n" + HELP_COMMANDS[module_name]
            await message.reply_text(HELP, parse_mode="md", disable_web_page_preview=True)
            await message.delete()
        except Exception as ef:
            await message.edit_text(f"<b>Error:</b>\n\n{ef}")
    else:
        await message.edit_text(f"Use `{HANDLER}help` to view help")
    return
