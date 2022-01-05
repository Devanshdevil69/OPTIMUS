from OPTIMUS import amaan, HANDLER
from pyrogram import filters

@amaan.on_message(filters.command("ls", HANDLER) & filters.me)
async def ls(client, message):
    args = message.text.split(None, 1)
    if len(args) == 2:
        basepath = "OPTIMUS/{}".format(args[1])
    else:
        basepath = "OPTIMUS/"
    directory = ""
    listfile = ""
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            directory += "\n{}".format(entry)
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            listfile += "\n{}".format(entry)
    await message.edit_text("**List directory :**`{}`\n**List file :**`{}`".format(directory, listfile))
