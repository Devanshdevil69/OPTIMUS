import asyncio
from OPTIMUS import amaan, HANDLER
from pyrogram import filters

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**FUN MODULES**
• {HANDLER}kill
• {HANDLER}mf
"""

# KiLL

@amaan.on_message(filters.command("kill", HANDLER) & filters.me)
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
