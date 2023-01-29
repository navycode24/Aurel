import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://telegra.ph//file/b5fa050775543872ae0ec.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴀᴋᴜ ҡʏɴλɴ ꭙ ꝛᴏʙᴏᴛ.** \n\n"
  TEXT += "๏ **ᴀᴋᴜ sᴇʟᴀʟᴜ ʜɪᴅᴜᴘ ᴅᴀɴ ʙᴇᴋᴇʀᴊᴀ** \n\n"
  TEXT += f"๏ **ᴍʏ ᴏᴡɴᴇʀ : [↻˹ҡʏɴλɴ˼𐦝](https://t.me/Riizzvbss)** \n\n"
  TEXT += f"๏ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"๏ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"๏ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/KynanUserbot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​", "https://t.me/Riizzvbss")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
