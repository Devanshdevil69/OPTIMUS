import asyncio
import os

os.system('clear')

import pyrogram
from pyrogram import Client


API_ID = int(input("enter Telegram API ID: "))
API_HASH = input("enter Telegram API HASH: ")
with Client(":memory:", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
        app.send_message(
            "me",
            f"#STRING_SESSION\n\n`{app.export_session_string()}`\n\n **TAP TO COPY**"
        )
        print("Done !, session string has been sent to saved messages!")
