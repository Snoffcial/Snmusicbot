# Power By@simpleearningprofit
# Join @snmusic1 For More Update
# Join @simpleearningprofit For Hack
# Join Our Chats @snmusic1 &@simpleearningprofit


from pyrogram import filters
from pyrogram.types import Message

from Snteam.config import BANNED_USERS
from Snteam.Bgt import get_command
from Snteam import app
from Snteam.core.call import Snteamh
from Snteam.utils.database import is_music_playing, music_off
from Snteam.utils.decorators import AdminRightsCheck
from Snteam.utils.inline.play import close_keyboard

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Snteamh.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )


# Power By@simpleearningprofit
# Join @snmusic1 For More Update
# Join @simpleearningprofit For Hack
# Join Our Chats @snmusic1 &@simpleearningprofit