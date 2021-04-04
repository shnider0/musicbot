from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
اهلا بك في بوت الموسيقى 
😉


الاوامر الخاصة بتشغيل البوت في المجموعة :
⚜️ /play - __لتشغيل الملفات الصوت بواسطة الرد او رابط يوتيوب .__
⚜️ /pause - __ايقاف صوت الموسيقى مؤقتا.__
⚜️ /resume - __استئناف الموسقى .__
⚜️ /skip - __الانتقال الى اللموسقى التالية.__
⚜️ /stop - __توقف الموسيقى.__
        يمكنك ايضا مراسلة المطور وطلب نسختك الخاصة من البوت 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "كروب المطور  💬", url="https://t.me/BOT_MUSIC_IQ"
                    ),
                    InlineKeyboardButton(
                        "قناة المطور  📣", url="https://t.me/BOTS_MUSIC_IQ "
                    ),
                    InlineKeyboardButton(
                        "القناة مميزة  📣", url="https://t.me/qad3im"
                    )
                ]
            ]
        )
    )
