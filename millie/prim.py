from pyrogram import Client, filters
from utils import temp
from pyrogram.types import Message
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import SUPPORT_CHAT

async def paid_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.PRIM_USERS

paid_user = filters.create(paid_users)

async def paid_chat(_, client, message: Message):
    return message.chat.id in temp.PRIM_CHATS

paid_group=filters.create(paid_chat)


@Client.on_message(filters.private & paid_user & filters.incoming)
async def paid_reply(bot, message):
    paid = await db.get_paid_status(message.from_user.id)
    await message.reply(f'congratulations 🎉 you are add PRIME USER to use Me. \npaid pkg: {paid["paid_reason"]}')

@Client.on_message(filters.group & paid_group & filters.incoming)
async def grp_bd(bot, message):
    buttons = [[
        InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    vazha = await db.get_chat(message.chat.id)
    k = await message.reply(
        text=f"CHAT ADDED TO PRIMUM CHAT 🐞\n\nMy admins has told me to give prime permission to working here ! If you want to know more about it contact support..\nReason : <code>{vazha['reason']}</code>.",
        reply_markup=reply_markup)
    try:
        await k.pin()
    except:
        pass
