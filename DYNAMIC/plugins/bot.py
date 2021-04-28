"""
✘ Commands Available
• `{i}alive`
    Check if your bot is working.
• `{i}ping`
    Check DYNAMICs response time.
• `{i}cmds`
    View all plugin names.
• `{i}restart`
    s - soft restart
    To restart your bot.
• `{i}logs`
    Get the last 100 lines from heroku logs.
• `{i}usage`
    Get app usage details.
• `{i}shutdown`
    Turn off your bot.
"""

import math
import shutil
import time
from datetime import datetime as dt
from platform import python_version as pyver

import heroku3
import requests
from git import Repo
from DYNAMIC import util
from telethon import __version__
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

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


@admin_cmd(
    pattern="ping$",
)
async def _(event):
    start = dt.now()
    x = await eor(event, "`Pong !`")
    end = dt.now()
    ms = (end - start).microseconds / 1000
    uptime = grt(time.time() - start_time)
    await x.edit(get_string("ping").format(ms, uptime))


@admin_cmd(
    pattern="cmds$",
)
async def cmds(event):
    await allcmds(event)


@admin_cmd(
    pattern="restart$",
)
async def restartbt(ult):
    if not Var.HEROKU_API:
        await eor(ult, "`Restarting..`")
        await bash("pkill python3 && python3 -m DYNAMIC")
    else:
        await restart(ult)




@admin_cmd(
    pattern="shutdown$",
)
async def shht(event):
    await eor(event, get_string("shutdown").format(OWNER_NAME))
    await ultroid_bot.disconnect()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
