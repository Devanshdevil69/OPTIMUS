import os
from OPTIMUS import LOGGER, load_cmds
from OPTIMUS import amaan

from OPTIMUS.modules import ALL_PLUGINS
from pyrogram import Client

async def start(self):
    await super().start()
    result = load_cmds(ALL_PLUGINS)
    log.info(result)

if __name__ == "__main__":
    amaan.run()
    amaan.idle()
