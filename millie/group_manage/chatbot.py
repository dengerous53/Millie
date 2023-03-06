from asyncio import gather, sleep
from info import *
from pyrogram import filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from aiohttp import ClientSession
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

ARQ_API_KEY = "XKCIMS-WNUNYK-BJFTHJ-YMMCKY-ARQ"
ARQ_API_URL = "https://arq.hamker.in"
USERBOT_PREFIX = "."
chatbot_group = 2
aiohttpsession = ClientSession()
active_chats_bot = []
active_chats_ubot = []
BOT_ID = int(BOT_TOKEN.split(":")[0])
SUDOERS = ADMINS
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

LOGGER.info("Gathering profile info")
x = app.get_me()
y = app2.get_me()

BOT_USERNAME = x.username
USERBOT_ID = y.id

async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


async def chat_bot_toggle(db, message: Message):
    status = message.text.split(None, 1)[1].lower()
    chat_id = message.chat.id
    if status == "enable":
        if chat_id not in db:
            db.append(chat_id)
            text = "Chatbot Enabled!"
            return await eor(message, text=text)
        await eor(message, text="ChatBot Is Already Enabled.")
    elif status == "disable":
        if chat_id in db:
            db.remove(chat_id)
            return await eor(message, text="Chatbot Disabled!")
        await eor(message, text="ChatBot Is Already Disabled.")
    else:
        await eor(message, text="**Usage:**\n/chatbot [ENABLE|DISABLE]")


# Enabled | Disable Chatbot


@Client.on_message(filters.command("chatbot") & ~filters.edited)
async def chatbot_status(_, message: Message):
    if len(message.command) != 2:
        return await eor(message, text="**Usage:**\n/chatbot [ENABLE|DISABLE]")
    await chat_bot_toggle(active_chats_bot, message)


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


async def type_and_send(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(3))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")


@Client.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.edited,
    group=chatbot_group,
)
async def chatbot_talk(_, message: Message):
    if message.chat.id not in active_chats_bot:
        return
    if not message.reply_to_message:
        return
    if not message.reply_to_message.from_user:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    await type_and_send(message)


# FOR USERBOT


@Client.on_message(
    filters.command("chatbot", prefixes=USERBOT_PREFIX)
    & ~filters.edited
    & SUDOERS
)
async def chatbot_status_ubot(_, message: Message):
    if len(message.text.split()) != 2:
        return await eor(message, text="**Usage:**\n.chatbot [ENABLE|DISABLE]")
    await chat_bot_toggle(active_chats_ubot, message)


@Client.on_message(
    ~filters.me & ~filters.private & filters.text & ~filters.edited,
    group=chatbot_group,
)
async def chatbot_talk_ubot(_, message: Message):
    if message.chat.id not in active_chats_ubot:
        return
    username = "@" + str(USERBOT_USERNAME)
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        if (
                message.reply_to_message.from_user.id != USERBOT_ID
                and username not in message.text
        ):
            return
    else:
        if username not in message.text:
            return
    await type_and_send(message)


@Client.on_message(
    filters.text & filters.private & ~filters.me & ~filters.edited,
    group=(chatbot_group + 1),
)
async def chatbot_talk_ubot_pm(_, message: Message):
    if message.chat.id not in active_chats_ubot:
        return
    await type_and_send(message)
