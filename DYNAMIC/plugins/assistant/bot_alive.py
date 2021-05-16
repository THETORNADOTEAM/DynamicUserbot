
from telethon import events
from DYNAMIC import ALIVE_NAME
from DYNAMIC import bot

PM_IMG = "https://telegra.ph/file/f7a8575e7242f1eb2e3f8.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.21.5' \n"
pm_caption += "➥ **Python:** `3.9.2` \n"
pm_caption += "➥ **Current Branch** : `main`\n"
pm_caption += f"➥ **ASSISTANT VERSION** : `1.0`\n"
pm_caption += "➥ **ASSISTANT VERSION** : `1.0 STABLE`\n\n"
pm_caption += "➥ **DYNAMIC USERBOT VERSION** : `1.0 STABLE`\n\n"
pm_caption += "➥ **Copyright** : By [TEAM DYNAMIC 2021 - 2022](https://github.com/TeamDynamic/Dynamic-Userbot)\n"
pm_caption += "[Assistant By DYNAMIC USERBOT ]"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def jarvis(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)

# PING
@tgbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
