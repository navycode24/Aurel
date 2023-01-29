import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://telegra.ph/file/1be0ff236e8c3de2772c4.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴀᴋᴜ ʜɪᴋᴀʀɪ ʀᴏʙᴏᴛ.** \n\n"
  PRIME += "🌼 **ᴀᴋᴜ sᴇʟᴀʟᴜ ʜɪᴅᴜᴘ ᴅᴀɴ ʙᴇᴋᴇʀᴊᴀ** \n\n"
  PRIME += f"🌼 **ᴍʏ ᴅᴀʀʟɪɴɢ : [ʀᴇxᴧ-ᴇx](https://t.me/JustRex)** \n\n"
  PRIME += f"🌼 **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  PRIME += f"🌼 **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  PRIME += f"🌼 **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  PRIME += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/HikariManageRobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/rexaprivateroom")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
