from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Hikari import pbot
from Hikari.utils.errors import capture_err
from Hikari.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("hikariinfo"))
async def repo(_, message):
    await message.reply_text(
        f"""🌺 **Hey Saya Hikari Robot** 
**ᴏᴡɴᴇʀ :** [ʀᴇxᴧ](https://t.me/JustRex)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`
**ʜɪᴋᴀʀɪ ʀᴏʙᴏᴛ ᴍᴀɴᴀɢᴇ ᴅᴀɴ ᴍᴜsɪᴄ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/tirexgugel"), 
                    InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/rexaprivateroom")
                ]
            ]
        ),
        disable_web_page_preview=True
    )
