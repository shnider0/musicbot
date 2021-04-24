from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>حبيبي 🥳 {message.from_user.first_name}!
 IQMUSICBOTS 
 @C5C5C5 

 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/Music-IQBOT-04-06",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/BOT_MUSIC_IQ"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://t.me/BOTS_MUSIC_IQ"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join ChatGroup", url="https://t.me/BOTS_MUSIC_IQ"
                    )
                ]
            ]
        )
    )

