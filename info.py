import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time
from logging import WARNING, getLogger
from telethon import TelegramClient
import heroku3 as HEROKU
import logging

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://te.legra.ph/file/5b2ec8d541fee97e63037.jpg https://te.legra.ph/file/14cea0c96e38ca47aca1c.jpg https://te.legra.ph/file/dad19fa5c940e89ec74aa.jpg https://te.legra.ph/file/727661d762e4aa3176e06.jpg https://te.legra.ph/file/a3cfa1226dab427486dd7.jpg https://te.legra.ph/file/ba56e6f9bf8f8638a5fb6.jpg https://te.legra.ph/file/24e85054dad2adc145961.jpg https://te.legra.ph/file/cc2842ea31dbeac22e8a5.jpg https://te.legra.ph/file/500ba5fb6ec16b4cabb28.jpg https://te.legra.ph/file/ba003b3cd73cfb7deb697.jpg https://te.legra.ph/file/4cf8d8e436f5a2dec30c1.jpg https://te.legra.ph/file/89249bc2f5b7a4473695b.jpg https://te.legra.ph/file/218b6cf8d19add39b0f19.jpg https://te.legra.ph/file/dd1d29623c4ed084fc2f7.jpg https://te.legra.ph/file/966eea5237847017ae209.jpg https://te.legra.ph/file/78c506103922f06291427.jpg https://te.legra.ph/file/5f07f995260d4036b562e.jpg https://te.legra.ph/file/6a0e9cba9eb2f326a9782.jpg https://te.legra.ph/file/24224bd1cd9524e870033.jpg https://te.legra.ph/file/0d6303364d49cd20612fc.jpg https://te.legra.ph/file/000469af1adb1dc0d4045.jpg https://te.legra.ph/file/614f3f0c080eb81736b15.jpg https://te.legra.ph/file/1b565643d97bd8d6e1f35.jpg')).split()
BOT_START_TIME = time()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/7d7cbf0d6c39dc5a05f5a.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/b58f576fed14cd645d2cf.jpg")

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/e54cae941b9b81f13eb71.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"")



# Admins, Channels & Users
OWNER_ID = environ.get('OWNER_ID', 5157282689)
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5157282689').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5157282689').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Millie")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '👋 Hello {user}\n\nmy name is {bot},\n just add me in your group i will better manage your group & some extra power with {bot} \n\nrose bot is nothing for me')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "rKJPufiXUL3twbCZuLaBw2z3")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://te.legra.ph/file/5b2ec8d541fee97e63037.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = bool(environ.get("PMFILTER", False))
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", True))
#url links
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '3a3935e37c74a2384f7a689c414f078ab6320785')

IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False)) if query.from_user.id in ADMINS:
                                                        else:
                                                            await query.answer("Your Not Authorizer ⚠️", show_alert=True)


# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001547941154))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'millie_robot_update')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_BTN = int(environ.get('MAX_BTN', "10"))
S_GROUP = environ.get('S_GROUP',"")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/millie_robot_update")
FILE_FORWARD = environ.get('FILE_FORWARD',"")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001547941154')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
    
SESSION_STRING = "1BJWap1sBuzNehGtsV99qoGF8ICaLfjg5VzVWgBCHmcm_fjmYB5T8mKleh2P63JASV6BGY9dikr80IdHhwh1ZbVSGYOhWOntH6ThDWegMIgza7pkVbDLWeOoxb9ueWiWUj-RA8CLRlziCDGN07bkyN1U9xcs4d1mdpbzM2BLgC1cnGl7y8CNRM8pTgx4TqfvJ53JHo3HuhABnY5OdL3_PkXOrTrT2M-hEBn1HKrXUo9cHuy-qYowdeYWxe4AlXNI3wRKjKI2cBToq7i5M8NRuCt2O6zAmBcgSQWM5uOWRl-85aJrmgZL6Shf_SoBOCEBxFGj9QmqXBBBYocaGn3BnpE-Zap2gnnw=" 
     # for short link 
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '74ec4052b0b4e419aa2d62437cd699b594423853')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 1000))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "HOW TO DOWNLOAD"
DOWNLOAD_TEXT_URL = "https://telegram.me/Movies_Web0"

   # Custom Caption Under Button #
CAPTION_BUTTON = "JOIN BACKUP"
CAPTION_BUTTON_URL = "https://telegram.me/Movies_Web0"


app = Client(
    "app2", 
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH)
LOGGER.info("Starting bot client")
app.start()

#log srt
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


