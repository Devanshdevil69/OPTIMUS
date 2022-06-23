# Code of @ARPiTax
# iDea oF @CRiMiNaL786
# To ReCovER His LosT AccoUNT of @GaNGsTeR_xD

import os
import asyncio
from OPTIMUS import amaan, HANDLER ,SUDO_USERS
from pyrogram import filters

@amaan.on_message(filters.command("forward", HANDLER) & filters.me)
@amaan.on_message(filters.command("forward", HANDLER) & filters.user(SUDO_USERS))
async def forwader(client, message):
   a = await amaan.get_history(777000, limit=1)
   print(a[0].text)
