import time

import heroku3
import requests
from telethon import __version__
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from DYNAMIC.utils import admin_cmd, sudo_cmd as ultroid_cmd


from . import *

HEROKU_API = None
HEROKU_APP_NAME = None

try:
    if Var.HEROKU_API and Var.HEROKU_APP_NAME:
        HEROKU_API = Var.HEROKU_API
        HEROKU_APP_NAME = Var.HEROKU_APP_NAME
        Heroku = heroku3.from_key(Var.HEROKU_API)
        heroku_api = "https://api.heroku.com"
        app = Heroku.app(Var.HEROKU_APP_NAME)
except BaseException:
    HEROKU_API = None
    HEROKU_APP_NAME = None

@ultroid_cmd(
    pattern="restart$",
)
async def repo(event):
    if Var.HEROKU_API:
        await eor(ult, "`Restarting..`")
        try:
            await restart(ult)
        except BaseException:
            await bash("pkill python3 && python3 -m DYNAMIC")
    else:
        await bash("pkill python3 && python3 -m DYNAMIC")

