from gpytranslate import Translator
from telegram.ext import CommandHandler, CallbackContext
from telegram import (
    Message,
    Chat,
    User,
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from Hikari import dispatcher, pbot
from pyrogram import filters
from Hikari.modules.disable import DisableAbleCommandHandler


__help__ = """ 
Gunakan modul ini untuk menerjemahkan bahasa!
*perintah:*
❂ /tl (atau /tr): sebagai balasan pesan, terjemahkan ke bahasa Inggris.
❂ /tl <lang>: diterjemahkan menjadi <lang>
misalnya: /tl ja: diterjemahkan ke dalam bahasa Jepang.
❂ /tl <source>//<dest>: diterjemahkan dari <source> ke <lang>.
misalnya:  /tl ja//en: menerjemahkan dari bahasa Jepang ke bahasa Inggris.
❂ /langs: dapatkan daftar bahasa yang didukung untuk terjemahan.
Saya dapat mengubah teks menjadi suara dan suara menjadi teks..
❂ /tts <lang code>*:* Balas pesan apa pun untuk mendapatkan output teks ke ucapan
❂ /stt*:* Ketik membalas pesan suara (hanya mendukung bahasa Inggris) untuk mengekstrak teks darinya.
*Kode bahasa*
`af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu`
"""

__mod_name__ = "ᴛʀᴀɴsʟᴀᴛᴇ"


trans = Translator()


@pbot.on_message(filters.command(["tl", "tr"]))
async def translate(_, message: Message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Balas pesan untuk menerjemahkannya!")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>Diterjemahkan dari {source} ke {dest}</b>:\n"
        f"<code>{translation.text}</code>"
    )

    await message.reply_text(reply, parse_mode="html")


def languages(update: Update, context: CallbackContext) -> None:
    update.effective_message.reply_text(
        "Klik tombol di bawah untuk melihat daftar kode bahasa yang didukung.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Kode bahasa",
                        url="https://telegra.ph/Lang-Codes-03-19-3",
                    ),
                ],
            ],
            disable_web_page_preview=True,
        ),
    )


LANG_HANDLER = DisableAbleCommandHandler("langs", languages, run_async=True)

dispatcher.add_handler(LANG_HANDLER)
