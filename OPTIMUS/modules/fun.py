import os
import asyncio
from OPTIMUS import amaan, HANDLER
from OPTIMUS.helpers.sudo import sudo_handler
from pyrogram import filters

__PLUGIN__ = "FUN"
__HELP__ = f"""
**FUN MODULES**
• {HANDLER}kill
• {HANDLER}mf
"""

# KiLL

@amaan.on_message(filters.command("kill", HANDLER) & filters.me)
@sudo_handler
async def kill(client, message):
   await message.edit_text("UseR KilleD Sucessfully  ▀̿ ̿Ĺ̯̿̿▀̿ ̿")

# MF

@amaan.on_message(filters.command("mf", HANDLER) & filters.me)
async def mf(client, message):
   await message.edit_text(
            "\n...................................../´¯/) "
            "\n...................................,/¯../ "
            "\n.................................../.../ "
            "\n................................../´.¯/"
            "\n................................./´¯./"
            "\n...............................,/¯../ "
            "\n.............................../.../ "
            "\n............................../´¯./"
            "\n............................./´¯./"
            "\n...........................,/¯../ "
            "\n.........................../.../ "
            "\n........................../´¯./"
            "\n........................./´¯./"
            "\n.......................,/¯../ "
            "\n......................./.../ "
            "\n....................../´¯./"
            "\n....................,/¯../ "
            "\n.................../..../ "
            "\n............./´¯/'...'/´¯¯`·¸ "
            "\n........../'/.../..../......./¨¯\ "
            "\n........('(...´...´.... ¯~/'...') "
            "\n.........\.................'...../ "
            "\n..........''...\.......... _.·´ "
            "\n............\..............( "
            "\n..............\.............\..."
        )


@amaan.on_message(filters.command("kill", SUDO_HANDLER) & filters(SUDO_USERS))
@sudo_handler
async def kill(client, message):
   await message.edit_text("UseR KilleD Sucessfully  ▀̿ ̿Ĺ̯̿̿▀̿ ̿")

# MF

@amaan.on_message(filters.command("mf", SUDO_HANDLER) & filters(SUDO_USERS))
async def mf(client, message):
   await message.edit_text(
            "\n...................................../´¯/) "
            "\n...................................,/¯../ "
            "\n.................................../.../ "
            "\n................................../´.¯/"
            "\n................................./´¯./"
            "\n...............................,/¯../ "
            "\n.............................../.../ "
            "\n............................../´¯./"
            "\n............................./´¯./"
            "\n...........................,/¯../ "
            "\n.........................../.../ "
            "\n........................../´¯./"
            "\n........................./´¯./"
            "\n.......................,/¯../ "
            "\n......................./.../ "
            "\n....................../´¯./"
            "\n....................,/¯../ "
            "\n.................../..../ "
            "\n............./´¯/'...'/´¯¯`·¸ "
            "\n........../'/.../..../......./¨¯\ "
            "\n........('(...´...´.... ¯~/'...') "
            "\n.........\.................'...../ "
            "\n..........''...\.......... _.·´ "
            "\n............\..............( "
            "\n..............\.............\..."
        )
