import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_IMG = ALIVE_IMG
else:
    DEADLY_IMG = "https://telegra.ph/file/c576171a46305e51f85c7.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "AFK SKYLORD"

OWNER_ID = config.OWNER_ID

Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/afk_community_ll"),
        Button.url("DEVELOPER", "https://t.me/Rajput_huhh")
        ],
        [
        Button.url("KHUD BNA LE BSDK", 
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[『SUPRA』|SUPRA](tg://user?id={6398607708})"
        DEADLY_ON = f"""
SUPRA {mention},
SUPRA:- {creator}!

AFK-SKYLORD:- {myOwner}

SUPRA:- {creator}

 """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
