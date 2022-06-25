import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_video("https://telegra.ph/file/0907dd7fcd6dfdfa65fe0.mp4")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
**ده بوت اغاني بس مش هكتر**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☬ اضفني الى مجموعتك ☬", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "𖤽𝙑𝙀𝙉𝙊𝙈𖤽", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "دٓيــفـݪ .ꨄ. ⁽️. ⁽𝒅𝒆𝒗𝒊𝒍", url=f"https://t.me/XH_0H"
                    )
                ],[
                    InlineKeyboardButton(
                        "ⓂⓄⒹⒺ", url=f"https://t.me/Y_M_4"
                    ),
                    InlineKeyboardButton(
                        ".", url="https://t.me/S_K_B"
                    )]
            ]
       ),
    )

