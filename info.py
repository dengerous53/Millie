import re
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

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

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://graph.org/file/e5d20bf124a2ff2671d82.jpg https://graph.org/file/a5c0673ca38cfa68a8727.jpg https://graph.org/file/0c05a363be872bfa723a3.jpg https://graph.org/file/847b4027ddd4c2a667e5b.jpg https://graph.org/file/3bd0228c20c29870b420a.jpg https://graph.org/file/887a542c8ce9ebd6b2c7c.jpg https://graph.org/file/ae54c55b0f2629fa29636.jpg https://graph.org/file/5d1c5d90a99912a940fb5.jpg https://graph.org/file/02ed2944177898bfe7fbb.jpg https://graph.org/file/76a53107accf5845bb966.jpg https://graph.org/file/e0571acdb0a8b1bb109c8.jpg https://graph.org/file/70f6f2f44a5013d1b39f6.jpg https://graph.org/file/8637afa785d7401d926da.jpg https://graph.org/file/1eb11f7565924258b7e24.jpg https://graph.org/file/87323376ffe837aab390c.jpg https://graph.org/file/b968fc9829b58afdbf446.jpg https://graph.org/file/7940635ffa142a1964546.jpg https://graph.org/file/2badac933abc11e22f7e1.jpg https://graph.org/file/254cad7be82d290799a62.jpg https://graph.org/file/b5f92b1313e538e18101d.jpg https://graph.org/file/50e42f9e2fbf8b973a175.jpg https://graph.org/file/b4765ce9dcf74e103e505.jpg https://graph.org/file/f507481d2cc30fba73d30.jpg https://graph.org/file/341bfefbb54a1bbb349c1.jpg https://graph.org/file/dac7285f398f0e15ec9f2.jpg https://graph.org/file/35633a52fe3fe2b237ed3.jpg https://graph.org/file/49a06f39a0e9ba6cc116f.jpg https://graph.org/file/707689413ddf9142b95e1.jpg https://graph.org/file/5398bd46f49b951d0f451.jpg https://graph.org/file/171e9c19e080e9e7fcdb4.jpg https://graph.org/file/5291f9e4b119f1cd878b9.jpg https://graph.org/file/e441c7ce8874e1028a4c7.jpg https://graph.org/file/eefff86d60f999cd86d28.jpg https://graph.org/file/f8055c23e9d6284c1bdec.jpg https://graph.org/file/1f1f7d26047ca52af5182.jpg https://graph.org/file/98e5064246a07cc606510.jpg https://graph.org/file/2438cdb76281c518ce70c.jpg https://graph.org/file/7f1789a1fda6acd5afd91.jpg https://graph.org/file/391cfdedaff7051e55798.jpg https://graph.org/file/e32e12b3375323a58fd93.jpg https://graph.org/file/e1ae32a1a02f510b590a8.jpg https://graph.org/file/4c741a4ffae24aeae487d.jpg https://graph.org/file/f9af65fc8610d6269f7cd.jpg https://graph.org/file/0e02106426bee5f9ee762.jpg https://graph.org/file/d0870d596ff2fe5231963.jpg https://graph.org/file/b16eafbb7e2994f93d63c.jpg https://graph.org/file/c6fd06ee56b728cffe6c5.jpg https://graph.org/file/57c49b2292420aeff5989.jpg https://graph.org/file/2538b58cabf6e2bfe03ed.jpg https://graph.org/file/9ee2300add1d3f7d687e0.jpg https://graph.org/file/a0141d0f27e64d2339ea8.jpg https://graph.org/file/2a8d87ab74b7db0ac9b90.jpg https://graph.org/file/a6f5dc9ba782536ff30ca.jpg https://graph.org/file/3de638755e67b0d6178a5.jpg https://graph.org/file/c17df80ef3fed418c82a1.jpg https://graph.org/file/d9b4d68656adc96f853df.jpg https://graph.org/file/11ffdf0e92cb270e1a223.jpg https://graph.org/file/1f6f62f8b7f7925b7375c.jpg https://graph.org/file/912d098b17e1af8a6f479.jpg https://graph.org/file/11b159078dda21521f67d.jpg https://graph.org/file/a6ea663a562c94f07a97b.jpg https://graph.org/file/793b792e8276cec110aaf.jpg https://graph.org/file/3fff5910444babcd8607c.jpg https://graph.org/file/37cb9fd88d94d46267238.jpg https://graph.org/file/5c4ffbcf12edd1da7302f.jpg https://graph.org/file/953d74f585897881e0b4c.jpg https://graph.org/file/7e4fea4dcdf2d684ea78a.jpg https://graph.org/file/a14cc9ba40c0ce35cc7da.jpg https://graph.org/file/a48f7821647e8a79b1cf3.jpg https://te.legra.ph/file/5b2ec8d541fee97e63037.jpg https://graph.org/file/610c559984550b438eb1c.jpg https://te.legra.ph/file/14cea0c96e38ca47aca1c.jpg https://te.legra.ph/file/dad19fa5c940e89ec74aa.jpg https://te.legra.ph/file/727661d762e4aa3176e06.jpg https://te.legra.ph/file/a3cfa1226dab427486dd7.jpg https://te.legra.ph/file/ba56e6f9bf8f8638a5fb6.jpg https://te.legra.ph/file/24e85054dad2adc145961.jpg https://te.legra.ph/file/cc2842ea31dbeac22e8a5.jpg https://te.legra.ph/file/500ba5fb6ec16b4cabb28.jpg https://te.legra.ph/file/ba003b3cd73cfb7deb697.jpg https://te.legra.ph/file/4cf8d8e436f5a2dec30c1.jpg https://te.legra.ph/file/89249bc2f5b7a4473695b.jpg https://te.legra.ph/file/218b6cf8d19add39b0f19.jpg https://te.legra.ph/file/dd1d29623c4ed084fc2f7.jpg https://te.legra.ph/file/966eea5237847017ae209.jpg https://te.legra.ph/file/78c506103922f06291427.jpg https://te.legra.ph/file/5f07f995260d4036b562e.jpg https://te.legra.ph/file/6a0e9cba9eb2f326a9782.jpg https://te.legra.ph/file/24224bd1cd9524e870033.jpg https://te.legra.ph/file/0d6303364d49cd20612fc.jpg https://te.legra.ph/file/000469af1adb1dc0d4045.jpg https://te.legra.ph/file/614f3f0c080eb81736b15.jpg https://te.legra.ph/file/1b565643d97bd8d6e1f35.jpg https://graph.org/file/22b4b99bc0ed5b505185a.jpg https://graph.org/file/29ed779f66f8f488d9aa8.jpg https://graph.org/file/cd471bc0a9e6c5cba86b7.jpg https://graph.org/file/16a713ab953dde31ac9a1.jpg https://graph.org/file/d49e99e3e85806b18f6f3.jpg https://graph.org/file/050ec41e308f1cd62ea43.jpg https://graph.org/file/bb63400383054f1fe635d.jpg https://graph.org/file/22d9c2e8111b031e0a10b.jpg https://graph.org/file/dfb4e19fc4a8c94af1710.jpg https://graph.org/file/f586df9668e54fc3bcf21.jpg https://graph.org/file/02d2de9cb65ec43d54be2.jpg https://graph.org/file/8dbc9214ea7358d9bfcf1.jpg https://graph.org/file/a52bb6c172542c9b80d64.jpg https://graph.org/file/dcaa11fe7ebaf34894e4e.jpg https://graph.org/file/6d5ebf02bc1236693451d.jpg https://graph.org/file/60e9a522fbdfc5706e7e0.jpg https://graph.org/file/48893113eecd972a24ef3.jpg https://graph.org/file/faaf73637afefd9dc3479.jpg https://graph.org/file/953dbdc36e0230bebfb03.jpg https://graph.org/file/79e782f4b071955872a13.jpg https://graph.org/file/93f24c5cc50ee5fcb4ccf.jpg https://graph.org/file/2ff3ace81a41751d78afd.jpg https://graph.org/file/e316d6a469a97c44cef32.jpg https://graph.org/file/f3e60661df730ed50882d.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
OWNER_ID = environ.get('OWNER_ID', 5157282689)
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5157282689').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5157282689').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
support_chat_id = environ.get('SUPPORT_CHAT_ID')
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Millie")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = DATABASE_URI

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '👋 Hello {user}\n\nmy name is {bot},\n just add me in your group i will better manage your group & some extra power with {bot} \n\nrose bot is nothing for me')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://te.legra.ph/file/5b2ec8d541fee97e63037.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = bool(environ.get("PMFILTER", False))
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", True))
NOR_IMG = WELCOM_PIC
SPELL_IMG = WELCOM_PIC
MELCOW_IMG = WELCOM_PIC
MELCOW_VID = environ.get('MELCOW_VID',"")


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
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
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


SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '9ff6e1bac0a97a4594be4520ac15bcde76564d6a')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

      # URL Shortener 
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '9ff6e1bac0a97a4594be4520ac15bcde76564d6a')

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


