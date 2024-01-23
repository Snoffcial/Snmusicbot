# Power By@simpleearningprofit
# Join @snmusic1 For More Update
# Join @simpleearningprofit For Hack
# Join Our Chats @snmusic1 &@simpleearningprofit


from pyrogram import filters
from pyrogram.types import Message

from Snmusic.config import BANNED_USERS
from Snmusic.Bgt import get_command
from Snmusic import app
from Snmusic.core.call import Snmusich
from Snmusic.utils.database import set_loop
from Snmusic.utils.decorators import AdminRightsCheck
from Snmusic.utils.bgtmusic.bk import command
from Snmusic.utils.inline.play import close_keyboard

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Snmusich.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )



# Power By@simpleearningprofit
# Join @snmusic1 For More Update
# Join @simpleearningprofit For Hack
# Join Our Chats @snmusic1 &@simpleearningprofit
