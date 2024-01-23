# Power By@simpleearningprofit
# Join @snmusic1 For More Update
# Join @simpleearningprofit For Hack
# Join Our Chats @snmusic1 &@simpleearningprofit 

from pyrogram import filters
from pyrogram.types import Message

from Snteam.config import BANNED_USERS
from Snteam.utils.bgtmusic.bk import command
from Snteam import app
from Snteam.core.call import Snteamh
from Snteam.utils.database import is_muted, mute_off
from Snteam.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["unmute", "cunmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if not await is_muted(chat_id):
        return await message.reply_text("**🔊 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...**")
    await mute_off(chat_id)
    await Snteamh.unmute_stream(chat_id)
    await message.reply_text(
        "**🔊 𝐔𝐧𝐦𝐮𝐭𝐞𝐝 🌷 ...**".format(message.from_user.mention)
    )



# PoweredBy @SnteamHalder & @AdityaHalder 
# Join @SnteamGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
