from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Snteam.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from Snteam.Sn import get_command
from Snteam import app
from Snteam.core.call import Snteamh
from Snteam.utils import bot_sys_stats
from Snteam.utils.decorators.language import language
from Snteam.utils.inline.play import close_keyboard

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Snteamh.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=close_keyboard
    )
