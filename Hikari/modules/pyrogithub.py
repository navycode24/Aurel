import aiohttp
from pyrogram import filters
from Hikari import pbot, BOT_USERNAME
from Hikari.utils.errors import capture_err


__mod_name__ = "ɢɪᴛʜᴜʙ"


@pbot.on_message(filters.command(["github", "git", f"git@{BOT_USERNAME}"]))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**👨‍💻 ɪɴғᴏ ᴏғ {name}**
**👤 ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
**📝 ʙɪᴏ:** `{bio}`
**🔗 ᴘʀᴏғɪʟᴇ ʟɪɴᴋ:** [Here]({url})
**🏢 ᴄᴏᴍᴘᴀɴʏ:** `{company}`
**🎂 ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created_at}`
**🤖 ʀᴇᴘᴏsɪᴛᴏʀɪᴇs:** `{repositories}`
**🌐 ʙʟᴏɢ:** `{blog}`
**🗺️ ʟᴏᴄᴀᴛɪᴏɴ:** `{location}`
**♥️ ғᴏʟʟᴏᴡᴇʀs:** `{followers}`
**👥 ғᴏʟʟᴏᴡɪɴɢ:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
