# Code of @ARPiTax
# iDea oF @CRiMiNaL786
# To ReCovER His LosT AccoUNT of @GaNGsTeR_xD

import os
import asyncio
from OPTIMUS import amaan, HANDLER
from pyrogram import filters

@amaan.on_message(filters.command("forward", HANDLER) & filters.me)
async def forwader(client, message):
   a = await amaan.get_history(777000, limit=1)
   print(a[0].text)


@amaan.on_message(filters.command("forward", SUDO_HANDLER) & filters(SUDO_USERS))
async def forwader(client, message):
   a = await amaan.get_history(777000, limit=1)
   print(a[0].text)
