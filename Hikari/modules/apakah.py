import random
from Hikari.events import register
from Hikari import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Harus banget gua jawab?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
