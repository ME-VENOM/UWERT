import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as Anonymous
from config import SUDO_USERS

@Client.on_message(filters.command(["اذاعه", "اذاعة"]))
async def broadcast(_, message: Message):
    await message.delete()
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`بيعمل اهو...`")
        if not message.reply_to_message:
            await wtf.edit("**__اعمل ريبلاي على رساله__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in Anonymous.iter_dialogs():
            try:
                await Anonymous.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...` \n\n**ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛᴏ :** `{sent}` **ᴄʜᴀᴛs** \n**ꜰᴀɪʟᴇᴅ ɪɴ :** `{failed}` **ᴄʜᴀᴛs**")
                await asyncio.sleep(0.3)
            except:
                failed=failed+1
        await message.reply_text(f"**ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ** \n\n**ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛᴏ :** `{sent}` **ᴄʜᴀᴛs** \n**ꜰᴀɪʟᴇᴅ ɪɴ​ :** `{failed}` **ᴄʜᴀᴛs**")
