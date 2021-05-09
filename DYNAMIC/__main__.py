
from DYNAMIC import bot
import os
os.system("git clone https://github.com/DYNAMIC-OP/DYNAMIC_PLUGS.git ./")
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from DYNAMIC.utils import load_module
from DYNAMIC import LOAD_PLUG, BOTLOG_CHATID, LOGS
from DYNAMICOP import bot, xbot
from pathlib import Path
import asyncio
import telethon.utils
import sys
import os
from sys import argv
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, Button
from var import Var
from DYNAMIC.utils import load_module, load_pro
from DYNAMIC import LOAD_PLUG, BOTLOG_CHATID
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating DYNAMIC FOR RUNNING")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("DYNAMIC USERBOT STARED SUCESSFULLY")
        print("LOADING SOFTWARE")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Loading Software Completed")
        print("LOADING HIDDEN FILES")
    else:
        bot.start()

import glob



path = 'DYNAMIC/DYNAMIC/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))

path = 'DYNAMIC/DYNAMIC/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


import DYNAMIC._core

print("DYNAMIC LOADED HIDDEN FILES, SOFTWARE WITH SUCESS JOIN SUPPORT FOR MORE INFO @DYNAMICUSERBOTSUPPORT ")
print("SOFTWARE VERSION 0.1 ")
print("BUILD VERSION 6#B*WJD ")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
