import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", ""))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/code663/BRANDEDKING",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ANGEL_K_WORLD")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/IND_PAWAN")

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 700))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 700))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", 
    "https://te.legra.ph/file/f5874a49d5acb00a19a7a.jpg"
    "https://te.legra.ph/file/5bf629d10afd4af953585.jpg",
    "https://te.legra.ph/file/7a321b99fe99d9d8b5117.jpg",
    "https://te.legra.ph/file/c482a7e55b459ffe07502.jpg",
    "https://telegra.ph//file/0879fbdb307005c1fa8ab.jpg",
    "https://telegra.ph//file/19e3a9d5c0985702497fb.jpg",
    "https://telegra.ph//file/b5fa277081dddbddd0b12.jpg",
    "https://telegra.ph//file/96e96245fe1afb82d0398.jpg",
    "https://telegra.ph//file/fb140807129a3ccb60164.jpg",
    "https://telegra.ph//file/09c9ea0e2660efae6f62a.jpg",
    "https://telegra.ph//file/3b59b15e1914b4fa18b71.jpg",
    "https://telegra.ph//file/efb26cc17eef6fe82d910.jpg",
    "https://telegra.ph//file/ab4925a050e07b00f63c5.jpg",
    "https://telegra.ph//file/d169a77fd52b46e421414.jpg",
    "https://telegra.ph//file/dab9fc41f214f9cded1bb.jpg",
    "https://telegra.ph//file/e05d6e4faff7497c5ae56.jpg",
    "https://telegra.ph//file/1e54f0fff666dd53da66f.jpg",
    "https://telegra.ph//file/18e98c60b253d4d926f5f.jpg",
    "https://telegra.ph//file/b1f7d9702f8ea590b2e0c.jpg",
    "https://telegra.ph//file/7bb62c8a0f399f6ee1f33.jpg",
    "https://telegra.ph//file/dd00c759805082830b6b6.jpg",
    "https://telegra.ph//file/3b996e3241cf93d102adc.jpg",
    "https://telegra.ph//file/610cc4522c7d0f69e1eb8.jpg",
    "https://telegra.ph//file/bc97b1e9bbe6d6db36984.jpg",
    "https://telegra.ph//file/2ddf3521636d4b17df6dd.jpg",
    "https://telegra.ph//file/72e4414f618111ea90a57.jpg",
    "https://telegra.ph//file/a958417dcd966d341bfe2.jpg",
    "https://telegra.ph//file/0afd9c2f70c6328a1e53a.jpg",
    "https://telegra.ph//file/82ff887aad046c3bcc9a3.jpg",
    "https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
    "https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
    "https://telegra.ph//file/a7cba6e78bb63e1b4aefb.jpg",
    "https://telegra.ph//file/f8ba75bdbb9931cbc8229.jpg",
    "https://telegra.ph//file/07bb5f805178ec24871d3.jpg",
    "https://telegra.ph/file/ec0ed654f5f5cefc90f95.jpg",
    "https://telegra.ph/file/f6aa2a3659462401cb600.jpg",
    "https://telegra.ph/file/0c3d91bcf75524a844883.jpg",
    "https://telegra.ph/file/6c5df27e71e074f1c7123.jpg",
    "https://telegra.ph/file/ff2ddc282fe7868e3cf73.jpg",
    "https://telegra.ph/file/6130ea9373d5f60898a52.jpg",
    "https://telegra.ph/file/45e5da1eab8f5892981ca.jpg",
)


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/4a810f39923161933f6e0.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
