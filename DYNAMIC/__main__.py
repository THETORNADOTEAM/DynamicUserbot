# MADE BY AMAN PANDEY FOR Speedo USERBOT DONT KANG.
from Speedo import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from Speedo.utils import load_module
from Speedo.utils import start_assistant
from Speedo import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Speedo USERBOT STABLE VERSION STARTING")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Speedo USERBOT STARED SUCESSFULLY")
        print("LOADING SOFTWARE")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Loading Software Completed")
        print("LOADING HIDDEN FILES")
        print ('INSTALLING ALL STABLE VERSION OF Speedo USERBOT AND PLUGINS')
    else:
        bot.start()
import glob
path = 'Speedo/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   

#import glob

#path = 'Speedo/plugins/*.py'
#files = glob.glob(path)
#for name in files:
#    with open(name) as f:
#        path1 = Path(f.name)
#        shortname = path1.stem
#        load_module(shortname.replace(".py", ""))

import glob

path = 'Speedo/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import Speedo._core

print("Speedo LOADED HIDDEN FILES, SOFTWARE WITH SUCESS JOIN SUPPORT FOR MORE INFO @SpeedoUSERBOTSUPPORT ")
print("SOFTWARE VERSION 1.0 Stable")
print("DYNAIMIC BRANCH: Stable")
print(" TELETHON VERSION 1.21.1 ")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
