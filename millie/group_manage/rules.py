from pyrogram import filters, Client, enums
from database.rulesdb import Rules
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from utils import temp

admin_filter=enums.ChatMembersFilter.ADMINISTRATORS


@Client.on_message(filters.command("rules") & filters.group)
async def get_rules(Client: client, message: Message):
    db = Rules(message.chat.id)
    msg_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    rules = db.get_rules()
    if not rules:
        return await message.reply_text(_["rules1"])
    priv_rules_status = db.get_privrules()
    if priv_rules_status:
        pm_kb = ikb([[("Rules",f"https://t.me/{temp.U_NAME}?start=rules_{message.chat.id}","url")]])
        return await message.reply_text(_["rules2"],
            quote=True,
            reply_markup=pm_kb,
            reply_to_message_id=msg_id,
        )
    return await message.reply_text(f"The rules for <b>{message.chat.title} are:</b>\n {rules}",
        disable_web_page_preview=True,
        reply_to_message_id=msg_id,
    )
    


@Client.on_message(filters.command("setrules") & admin_filter)
async def set_rules(Client: client, message: Message):
    db = Rules(message.chat.id)
    if message.reply_to_message and message.reply_to_message.text:
        rules = message.reply_to_message.text.markdown
    elif (not message.reply_to_message) and len(message.text.split()) >= 2:
        rules = message.text.split(None, 1)[1]
    else:
        return await message.reply_text(_["rules3"])
    db.set_rules(rules)
    return await message.reply_text(_["rules4"])
    


@Client.on_message(filters.command(["pmrules", "privaterules"]) & admin_filter)
async def priv_rules(Client: client, message: Message):
    db = Rules(message.chat.id)
    if len(message.text.split()) == 2:
        option = (message.text.split())[1]
        if option in ("on", "yes"):
            db.set_privrules(True)
            msg = f"Private Rules have been turned <b>on</b> for chat <b>{message.chat.title}</b>"
        elif option in ("off", "no"):
            db.set_privrules(False)
            msg = f"Private Rules have been turned <b>off</b> for chat <b>{message.chat.title}</b>"
        else:
            msg = "Option not valid, choose from <code>on</code>, <code>yes</code>, <code>off</code>, <code>no</code>"
        await message.reply_text(msg)
    elif len(message.text.split()) == 1:
        curr_pref = db.get_privrules()
        msg = f"Current Preference for Private rules in this chat is: <b>{curr_pref}</b>"
        await message.reply_text(msg)
    else:
        return await message.replt_text(_["rules5"])


@Client.on_message(filters.command("clearrules") & admin_filter)
async def clear_rules(Client: client, message: Message):
    db = Rules(message.chat.id)
    rules = db.get_rules()
    if not rules:
        return await message.reply_text(_["rules1"])
    return await message.reply_text("Are you sure you want to clear rules?",
        reply_markup=ikb([[("⚠️ Confirm", "clear_rules"), ("❌ Cancel", "close_data")]]))
    

