from Snteam.core.bot import SnteamBot
from Snteam.core.dir import dirr
from Snteam.core.git import git
from Snteam.core.userbot import Userbot
from Snteam.misc import dbb, heroku

from .logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = SnteamBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
