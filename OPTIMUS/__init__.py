


import os
from pyrogram import Client
from datetime import datetime
#from plugins import *

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION_STRING"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
HANDLER = os.environ["HANDLER"]


# client

amaan = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

# assisstant client

amaan2 = Client("hehe", api_id=API_ID, api_hash=API_HASH, bot_token = BOT_TOKEN)

# start time

StartTime = datetime.now()
