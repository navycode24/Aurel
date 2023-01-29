import asyncio
import time
from telethon import events

from Hikari import telethn
from Hikari.modules.helper_funcs.telethn.chatstatus import (
    can_delete_messages,
    user_is_admin,
)


async def purge_messages(event):
    start = time.perf_counter()
    if event.from_id is None:
        return

    if (
        not await user_is_admin(
            user_id=event.sender_id,
            message=event,
        )
        and event.from_id not in [1087968824]
    ):
        await event.reply("Hanya Admin yang diperbolehkan menggunakan perintah ini")
        return

    if not await can_delete_messages(message=event):
        await event.reply("Sepertinya tidak dapat menghapus pesan")
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Balas pesan untuk memilih dari mana memulai pembersihan.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    try:
        await event.client.delete_messages(event.chat_id, messages)
    except:
        pass
    time_ = time.perf_counter() - start
    text = f"Purged Successfully in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode="markdown")

async def delete_messages(event):
    if event.from_id is None:
        return

    if (
        not await user_is_admin(
            user_id=event.sender_id,
            message=event,
        )
        and event.from_id not in [1087968824]
    ):
        await event.reply("Hanya Admin yang diperbolehkan menggunakan perintah ini")
        return

    if not await can_delete_messages(message=event):
        await event.reply("Sepertinya tidak bisa menghapus ini?")
        return

    message = await event.get_reply_message()
    if not message:
        await event.reply("Apa yang ingin di hapus?")
        return
    chat = await event.get_input_chat()
    del_message = [message, event.message]
    await event.client.delete_messages(chat, del_message)

PURGE_HANDLER = purge_messages, events.NewMessage(pattern="^[!/]purge$")
DEL_HANDLER = delete_messages, events.NewMessage(pattern="^[!/]del$")

telethn.add_event_handler(*PURGE_HANDLER)
telethn.add_event_handler(*DEL_HANDLER)

__mod_name__ = "Purges"
__command_list__ = ["del", "purge"]
__handlers__ = [PURGE_HANDLER, DEL_HANDLER]
