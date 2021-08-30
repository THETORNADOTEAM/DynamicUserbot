import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from DYNAMIC import ALIVE_NAME, StartTime
from DYNAMIC.utils import admin_cmd
from DYNAMIC import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from DYNAMIC.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from DYNAMIC import botnickname 
BOT = str(botnickname) if botnickname else "DYNAMIC USERBOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "DYNAMIC USER"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
DYNAMIC = "[DYNAMIC](https://t.me/OFFLINEMODEON)"
#my bots repo 👇
REPO = "[LEGEND BOT](https://github.com/TeamDynamic/Dynamic-Userbot)"
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/DYNAMICUSERBOTSUPPORT)"
ALIVE = "DYNAMIC USERBOT IS ON 🔥 FIRE 🔥" #make by LEGENDX22
OP = " HELLO MASTER MY NAME IS DYNAMIC I AM A BEST USERBOT 💝"
EMOJI = "🔥"
