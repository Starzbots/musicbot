import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCi3qX5_LX62zu0_IICAU3X5fmugiDq0mAMTCfIiPlg3S_f8aZwWpYXcaSmyS6Jp8LpSlIcigLgXyjS5uRG8QzHoN2RXWarDARZG8SUFF1XgH-82jFfJS0V4WoZK98y6OJI30NtkayuYXYgoRjdSrxVARtfOZt0fYsPA1cChZ5koN1HQswEtX_L4ke0kfY5MSf06Km2yNMlJOnznUAlHpb4PJW5qLh2PClXTo-aNfUWgyO5ZhDjybRx9z2xoFiHudibW5xiTBJGAgGMKt0qsyisY0-jM8otMxRtF0gQqrr9SOLNve8DANK2Y_HZwhPNkk5r4rTbGoAyQ--fSRTKWKk4fbIblgA")
BOT_TOKEN = getenv("BOT_TOKEN", "2100234484:AAH5lDwl8OIHFNGUCeCZe6w8Gcoirzdxt9k")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID", " 11461788))
API_HASH = getenv("API_HASH", "e090f8d649c80b63f6c0967689f4f160")
OWNER_NAME = getenv("OWNER_NAME", "Stargirl")
ALIVE_NAME = getenv("ALIVE_NAME", "Florenza")
BOT_USERNAME = getenv("BOT_USERNAME", "Florenza_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Florenzaassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "florenzasupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Starz_bots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Starzbots/muzik")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
