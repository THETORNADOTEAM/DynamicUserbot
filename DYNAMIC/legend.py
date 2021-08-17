import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from Speedo import ALIVE_NAME, StartTime
from Speedo.utils import admin_cmd
from Speedo import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from Speedo.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from Speedo import botnickname 
BOT = str(botnickname) if botnickname else "Speedo USERBOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Speedo USER"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
Speedo = "[Speedo](https://t.me/OFFLINEMODEON)"
#my bots repo 👇
REPO = "[LEGEND BOT](https://github.com/TeamDynamic/Dynamic-Userbot)"
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/SpeedoUSERBOTSUPPORT)"
ALIVE = "Speedo USERBOT IS ON 🔥 FIRE 🔥" #make by LEGENDX22
OP = " HELLO MASTER MY NAME IS Speedo I AM A BEST USERBOT 💝"
EMOJI = "🔥"
