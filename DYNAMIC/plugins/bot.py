import time

import heroku3
import requests
from telethon import __version__
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

@admin_cmd(
    pattern="restart$",
)
async def restartbt(ult):
    if Var.HEROKU_API:
        await eor(ult, "`Restarting..`")
        try:
            await restart(ult)
        except BaseException:
            await bash("pkill python3 && python3 -m DYNAMIC")
    else:
        await bash("pkill python3 && python3 -m DYNAMIC")

