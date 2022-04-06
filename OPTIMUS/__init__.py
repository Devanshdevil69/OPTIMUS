import importlib
import os
from pyrogram import Client
from datetime import datetime
#from plugins import *
import logging


API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION_STRING"]
LOGGER = logging.getLogger(__name__)
HANDLER = os.environ["HANDLER"]
ALL_PLUGINS = [ ]

# the logging things

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - [OPTIMUS] - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
log = logging.getLogger("[OPTIMUS]")
log.info("OPTIMUS Userbot | Powered By AMAAN THE GAMER KING | Licensed under GPLv3.")
log.info(" OPTIMUS is Started TRY .help or .alive ")

# client

amaan = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

# start time

StartTime = datetime.now()

# for help command

HELP_COMMANDS = {}
"""
def load_cmds(ALL_PLUGINS):
    for oof in ALL_PLUGINS:
        if oof.lower() == "help":
            continue
        imported_module = importlib.import_module("OPTIMUS.modules." + oof)
        if not hasattr(imported_module, "__PLUGIN__"):
            imported_module.__PLUGIN__ = imported_module.__name__

        if not imported_module.__PLUGIN__.lower() in HELP_COMMANDS:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )

        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module.__HELP__
    return "Done Loading Plugins and Commands!"
"""
# another help

for all_plugins in ALL_PLUGINS:
            imported_module = importlib.import_module(
                "OPTIMUS.modules." + all_plugins
            )
            if (
                hasattr(imported_module, "__PLUGIN__")
                and imported_module.__PLUGIN__
            ):
                imported_module.__PLUGIN__ = imported_module.__PLUGIN__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELP_COMMANDS[
                        imported_module.__PLUGIN__.lower()
                    ] = imported_module
