import asyncio
from telethon import events
from telethon.errors import MessageIdInvalidError
#from [ Made By Melo_Qt ] [event.import Meglavinia, from maxets import Telethon
@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if "Monster" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5) 
            await event.click(1, 0)  
        return

@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if "Monster" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5) 
            await event.click(1, 0) 
        return

@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if "Monster" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5)  
            await event.click(1, 0)  
        return


@bot.on(events.MessageEdited(from_users=5364964725))
async def _(event):
    if "Monster" in event.raw_text:
        try:
            await asyncio.sleep(0.5)  
            await event.click(1, 0)  
        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass

@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if "Level" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5)  
            await event.click(0) 
        return
        
@bot.on(events.MessageEdited(from_users=5364964725))
async def _(event):
    if "select one" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5)  
            await event.click(0) 
        return        

@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if "offers?" in event.raw_text:
        if event.buttons:
            await asyncio.sleep(0.5)  
            await event.click(0)  
        return

@bot.on(events.MessageEdited(from_users=5364964725))
async def _(event):
    try:
        if "Offers you" in event.raw_text:
            per_pearl = None
            per_ticket = None
            contains_other_items = False

            
            for line in event.raw_text.split("\n"):
                if "pearls for" in line:
                    per_pearl = int(line.split("for")[1].split("coins per")[0].strip())
                elif "tickets for" in line:
                    per_ticket = int(line.split("for")[1].split("coins per")[0].strip())
                elif any(item in line for item in ["rope", "net", "large net", "chain", "tranquilizer", "freeze ray"]):
                    contains_other_items = True

            if per_pearl and per_pearl > 200:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.client.send_message(5364964725, "/explore")
            elif per_ticket and per_ticket > 400:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.client.send_message(5364964725, "/explore")
            elif contains_other_items:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.client.send_message(5364964725, "/explore")
            elif per_pearl and per_pearl <= 200:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)  # Click the regular button (index 0, row 0)
            elif per_ticket and per_ticket <= 400:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0)  # Click the regular button (index 0)
    except (asyncio.TimeoutError, MessageIdInvalidError):
        pass
        
        
@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if any(keyword in event.raw_text for keyword in ["coins and grant", "Common", "Rare", "Wishing"]):
        await asyncio.sleep(0.5)  
        await event.client.send_message(5364964725, "/explore")
        
@bot.on(events.NewMessage(from_users=5364964725))
async def _(event):
    if any(keyword in event.raw_text for keyword in ["temple", "village", "rich"]):
        await asyncio.sleep(0.5)  
        await event.client.send_message(5364964725, "/start")
        await asyncio.sleep(1)  
        await event.client.send_message(5364964725, "/explore")        

@bot.on(events.MessageEdited(from_users=5364964725))
async def _(event):
    if "traded" in event.raw_text:
        await asyncio.sleep(1)
        await event.client.send_message(5364964725, "/explore")
        
    
