# ZINDA PLUGIN BANAYA HAI GODBOY NE 
# KANG MAT KARNA KOI BHI


from hashlib import sha256
from pyrogram import Client, filters
from pyrogram.types import Message
from Vinci import god
from pyromod import listen


async def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()
  
async def mine(block_number, transactions, previous_hash, prefix_zeros, MAX_NONCE):
  prefix_str = '0' + prefix_zeros
  for nonce in range(MAX_NONCE):
    text = str(block_number) + transactions + previous_hash + str(nonce)
    new_hash = await SHA256(text)
    if new_hash.startswith(prefix_str):
      print(f"Yay! Succesfully mined bitcoins with nonce value:- {nonce}")
      return new_hash


@god.on_message(filters.command("btc") & filters.private)
async def btc_mining(_, m: Message):
  block_number = await god.ask(m.chat.id, "**Send me the** __Block Number__")
  if block_number.text.startswith("/"):
    return
  else:
    pass
  transactions = await god.ask(m.chat.id, "**Now send me your** __Wallet Address__")
  if transactions.text.startswith("/"):
    return
  else:
    pass
  previous_hash = await god.ask(m.chat.id, "**Send me the** __Previous Hash__")
  if previous_hash.text.startswith("/"):
    return
  else:
    pass
  prefix_zeros = await god.ask(m.chat.id, "**Send me the value of** __Prefix Zeros__")
  if prefix_zeros.text.startswith("/"):
    return
  else:
    pass
  MAX_NONCE = await god.ask(m.chat.id, "**Ok now send the** __Nonce Value__")
  if MAX_NONCE.text.startswith("/"):
    return
  else:
    pass
  await god.send_message(m.chat.id, "__Started Mining__ \n**Please do not send any command**\n\n**Note:- If you send any command during Mining then your mining will stop and you have to do all the steps again**")
  hola = await mine(block_number, transactions, previous_hash, prefix_zeros, MAX_NONCE) 
  if hola:
    await god.send_message(m.chat.id, f"**Yay! Succesfully mined bitcoins with nonce value:- {nonce}**")
    await god.send_message(m.chat.id, new_hash)
  else:
    await god.send_message(m.chat.id, "Coudn't find correct hash after trying {MAX_NONCE} times")
  
  
