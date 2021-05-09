from DYNAMIC import bot
from Plugs import Plugs
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
os.system("pip install google_trans_new")
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
EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", True)
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)
ONLINE_ALERT = os.environ.get("ONLINE_ALERT")
os.system("pip install LEGENDX==0.0.21")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

import glob



path = 'DYNAMIC/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))


if  EXTRA_PLUGS == True:
    os.system("git clone https://github.com/DYNAMIC-OP/DYNAMIC_PLUGS.git ./")
    path = "*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:
  path = 'DYNAMIC/plugins/*.py'
  files = glob.glob(path)
  for name in files:
      with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_module(shortname.replace(".py", ""))


import DYNAMIC._core

print("🇾 🇴 🇺 🇷  🇺 🇸 🇪 🇷 🇴 🇹  🇮 🇸  🇼 🇴 🇷 🇰 🇮 🇳 🇬  🇫 🇮 🇳 🇪  🇵 🇱 🇿 .🇯 🇴 🇮 🇳 🇴 🇺 🇷 🇷  🇬 🇷 🇴 🇺 🇵  🇦 🇳 🇩  🇨 🇭 🇦 🇳 🇳 🇪 🇱 ")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
