#    @GODBOYX

#    Copyright ? 2021 TeamDynamic



#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or


#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

import asyncio



from telethon import events, functions

from telethon.tl.functions.users import GetFullUserRequest



import DYNAMIC.plugins.sql_helper.pmpermit_sql as DYNAMIC_sql

from DYNAMIC import ALIVE_NAME, bot

from DYNAMIC.DYNAMICConfig import Config

from var import Var

DYNAMICUSER = str(ALIVE_NAME) if ALIVE_NAME else "DYNAMIC USER"

from DYNAMIC.utils import admin_cmd as DYNAMIC_cmd



DYNAMIC_WRN = {}

DYNAMIC_REVL_MSG = {}



DYNAMIC_PROTECTION = os.environ.get("PM_PROTECT","yes")



SPAM = os.environ.get("SPAM", None)

if SPAM is None:

    HMM_LOL = "5"

else:

    HMM_LOL = SPAM



DYNAMIC_PM = os.environ.get("PMPERMIT_PIC", None)

CUSTOM_DYNAMIC_PM_PIC = DYNAMIC_PM

FUCK_OFF_WARN = f"**Blocked You As You Spammed {DYNAMICUSER}'s DM\n\n **IDC**"









OVER_POWER_WARN = (

    f"**Hello Sir Im Here To Protect {DYNAMICUSER} Dont Under Estimate Me 😈😈 **\n\n"

    f"`My Master {DYNAMICUSER} is Busy Right Now !` \n"

    f"{DYNAMICUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"

    f"**Btw Dont Spam Or Get Banned** 😈 \n\n"

    f"**{CUSTOM_DYNAMIC_PM_PIC}**\n"

)



DYNAMIC_STOP_EMOJI = (

    "â"

)

if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(events.NewMessage(outgoing=True))

    async def DYNAMIC_dm_niqq(event):

        if event.fwd_from:

            return

        chat = await event.get_chat()

        if event.is_private:

            if not DYNAMIC_sql.is_approved(chat.id):

                if not chat.id in DYNAMIC_WRN:

                    DYNAMIC_sql.approve(chat.id, "outgoing")

                    bruh = "Auto-approved bcuz outgoing 😗😗👍"

                    rko = await borg.send_message(event.chat_id, bruh)

                    await asyncio.sleep(3)

                    await rko.delete ()  



    @borg.on(DYNAMIC_cmd(pattern="(a|approve)"))

    async def block(event):

        if event.fwd_from:

            return

        replied_user = await borg(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chats = await event.get_chat()

        if event.is_private:

            if not DYNAMIC_sql.is_approved(chats.id):

                if chats.id in DYNAMIC_WRN:

                    del DYNAMIC_WRN[chats.id]

                if chats.id in DYNAMIC_REVL_MSG:

                    await DYNAMIC_REVL_MSG[chats.id].delete()

                    del DYNAMIC_REVL_MSG[chats.id]

                DYNAMIC_sql.approve(chats.id, f"Wow lucky You {DYNAMICUSER} Approved You")

                await event.edit(

                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)

                )

                await asyncio.sleep(3)

                await event.delete()



    @borg.on(DYNAMIC_cmd(pattern="block$"))

    async def DYNAMIC_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if DYNAMIC_sql.is_approved(chat.id):

                DYNAMIC_sql.disapprove(chat.id)

            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(4)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(3)

            await event.edit("ð [{}](tg://user?id={})".format(firstname, chat.id ))

            await event.client(functions.contacts.BlockRequest(chat.id))

            await event.delete()





    @borg.on(DYNAMIC_cmd(pattern="(da|disapprove)"))

    async def DYNAMIC_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if DYNAMIC_sql.is_approved(chat.id):

                DYNAMIC_sql.disapprove(chat.id)

            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("ð [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit(

                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)

                )

            await event.delete()







    @borg.on(DYNAMIC_cmd(pattern="listapproved$"))

    async def DYNAMIC_approved_pm(event):

        if event.fwd_from:

            return

        approved_users = DYNAMIC_sql.get_all_approved()

        PM_VIA_LIGHT = f"â¥â¿â¥ {DYNAMICUSER} Approved PMs\n"

        if len(approved_users) > 0:

            for a_user in approved_users:

                if a_user.reason:

                    PM_VIA_LIGHT += f"â¥â¿â¥ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"

                else:

                    PM_VIA_LIGHT += (

                        f"â¥â¿â¥ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"

                    )

        else:

            PM_VIA_LIGHT = "no Approved PMs (yet)"

        if len(PM_VIA_LIGHT) > 4095:

            with io.BytesIO(str.encode(PM_VIA_LIGHT)) as out_file:

                out_file.name = "approved.pms.text"

                await event.client.send_file(

                    event.chat_id,

                    out_file,

                    force_document=True,

                    allow_cache=False,

                    caption="Current Approved PMs",

                    reply_to=event,

                )

                await event.delete()

        else:

            await event.edit(PM_VIA_LIGHT)



    @borg.on(events.NewMessage(incoming=True))

    async def DYNAMIC_new_msg(DYNAMIC):

        if DYNAMIC.sender_id == bot.uid:

            return



        if Var.PRIVATE_GROUP_ID is None:

            return



        if not DYNAMIC.is_private:

            return



        DYNAMIC_chats = DYNAMIC.message.message

        chat_ids = DYNAMIC.sender_id



        DYNAMIC_chats.lower()

        if OVER_POWER_WARN == DYNAMIC_chats:

            # DYNAMIC should not reply to other DYNAMIC

            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots

            return

        sender = await bot.get_entity(DYNAMIC.sender_id)

        if chat_ids == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if DYNAMIC_PROTECTION == "NO":

            return

        if DYNAMIC_sql.is_approved(chat_ids):

            return

        if not DYNAMIC_sql.is_approved(chat_ids):

            # pm permit

            await DYNAMIC_goin_to_attack(chat_ids, DYNAMIC)



    async def DYNAMIC_goin_to_attack(chat_ids, DYNAMIC):

        if chat_ids not in DYNAMIC_WRN:

            DYNAMIC_WRN.update({chat_ids: 0})

        if DYNAMIC_WRN[chat_ids] == 3:

            lemme = await DYNAMIC.reply(FUCK_OFF_WARN)

            await asyncio.sleep(3)

            await DYNAMIC.client(functions.contacts.BlockRequest(chat_ids))

            if chat_ids in DYNAMIC_REVL_MSG:

                await DYNAMIC_REVL_MSG[chat_ids].delete()

            DYNAMIC_REVL_MSG[chat_ids] = lemme

            lightn_msg = ""

            lightn_msg += "#Some Retards ð\n\n"

            lightn_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"

            lightn_msg += f"Message Counts: {DYNAMIC_WRN[chat_ids]}\n"

            # lightn_msg += f"Media: {message_media}"

            try:

                await DYNAMIC.client.send_message(

                    entity=Var.PRIVATE_GROUP_ID,

                    message=lightn_msg,

                    # reply_to=,

                    # parse_mode="html",

                    link_preview=False,

                    # file=message_media,

                    silent=True,

                )

                return

            except BaseException:

                  await  DYNAMIC.edit("Something Went Wrong")

                  await asyncio.sleep(2) 

            return



        # Inline

        DYNAMICusername = Var.TG_BOT_USER_NAME_BF_HER

        DYNAMIC_L = OVER_POWER_WARN.format(

        DYNAMICUSER, DYNAMIC_STOP_EMOJI, DYNAMIC_WRN[chat_ids] + 1, HMM_LOL

        )

        DYNAMIC_hmm = await bot.inline_query(DYNAMICusername, DYNAMIC_L)

        new_var = 0

        yas_ser = await DYNAMIC_hmm[new_var].click(DYNAMIC.chat_id)

        DYNAMIC_WRN[chat_ids] += 1

        if chat_ids in DYNAMIC_REVL_MSG:

           await DYNAMIC_REVL_MSG[chat_ids].delete()

        DYNAMIC_REVL_MSG[chat_ids] = yas_ser







@borg.on(events.NewMessage(incoming=True, from_users=(1100231654)))

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DYNAMIC_sql.is_approved(chats.id):

            DYNAMIC_sql.approve(chats.id, "**GOD FATHER IS HERE**")

            await borg.send_message(

                chats, "**Heya @LEGENDX22 YOU ARE MY CREATOR I APPROVED YOU SIR ❤️🥰🔥⚜️**"

            )





@borg.on(
    events.NewMessage(incoming=True, from_users=(1100231654))
)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DYNAMIC_sql.is_approved(chats.id):

            DYNAMIC_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You @LEGENDX22 How Can I Disapprove You Come In Sir**ðð"

            )

            print("Dev Here")

@borg.on(
    events.NewMessage(incoming=True, from_users=(1100231654))
)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DYNAMIC_sql.is_approved(chats.id):

            DYNAMIC_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You master. How Can I Disapprove You Come In Sir**ðð"

            )            

@borg.on(
    events.NewMessage(incoming=True, from_users=(1100231654))
)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DYNAMIC_sql.is_approved(chats.id):

            DYNAMIC_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You . How Can I Disapprove You Come In Sir**ðð"

            )               

            print("Dev Here")





@borg.on(
    events.NewMessage(incoming=True, from_users=(1100231654))
)

async def krish_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DYNAMIC_sql.is_approved(chats.id):

            DYNAMIC_sql.approve(chats.id, "**Heya Sir**")

            await borg.send_message(

                chats, f"**Good To See You master. How Can I Disapprove You Come In Sir**ðð"

            )               

            print("Dev Here")
