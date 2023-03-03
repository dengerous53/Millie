from pyrogram import filters
from pyrogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

from millie import Bot
from millie.group_manage.rules_db import Rules
from millie.group_manage.tr_engine import tlang
from millie.helper.admin_check import admin_fliter
from utils import temp
import logging, WARNING
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.WARNING)

def ikb(rows=None):
    if rows is None:
        rows = []
    lines = []
    for row in rows:
        line = []
        for button in row:
            button = btn(*button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})

@Bot.on_message(filters.command("rules") & filters.group)
async def get_rules(_, m: Message):
    db = Rules(m.chat.id)
    msg_id = m.reply_to_message.id if m.reply_to_message else m.id

    rules = db.get_rules()
    LOGGER.info(f"{m.from_user.id} fetched rules in {m.chat.id}")
    if m and not m.from_user:
        return

    if not rules:
        await m.reply_text(
            (tlang(m, "rules.no_rules")),
            quote=True,
        )
        return

    if db.get_privrules():
        pm_kb = ikb(
            [
                [
                    (
                        "Rules",
                        f"https://t.me/{temp.U_NAME}?start=rules_{m.chat.id}",
                        "url",
                    ),
                ],
            ],
        )
        await m.reply_text(
            (tlang(m, "rules.pm_me")),
            quote=True,
            reply_markup=pm_kb,
            reply_to_message_id=msg_id,
        )
        return

    formated = rules

    await m.reply_text(
        (tlang(m, "rules.get_rules")).format(
            chat=f"<b>{m.chat.title}</b>",
            rules=formated,
        ),
        disable_web_page_preview=True,
        reply_to_message_id=msg_id,
    )
    return


@Bot.on_message(filters.command("setrules") & admin_filter)
async def set_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    if m.reply_to_message and m.reply_to_message.text:
        rules = m.reply_to_message.text.markdown
    elif (not m.reply_to_message) and len(m.text.split()) >= 2:
        rules = m.text.split(None, 1)[1]
    else:
        return await m.reply_text("Provide some text to set as rules !!")

    if len(rules) > 4000:
        rules = rules[:3949]
        await m.reply_text("Rules are truncated to 3950 characters!")

    db.set_rules(rules)
    LOGGER.info(f"{m.from_user.id} set rules in {m.chat.id}")
    await m.reply_text(tlang(m, "rules.set_rules"))
    return


@Bot.on_message(
    filters.command(["pmrules", "privaterules"]) & admin_filter,
)
async def priv_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    if len(m.text.split()) == 2:
        option = (m.text.split())[1]
        if option in ("on", "yes"):
            db.set_privrules(True)
            LOGGER.info(f"{m.from_user.id} enabled privaterules in {m.chat.id}")
            msg = tlang(m, "rules.priv_rules.turned_on").format(chat_name=m.chat.title)
        elif option in ("off", "no"):
            db.set_privrules(False)
            LOGGER.info(f"{m.from_user.id} disbaled privaterules in {m.chat.id}")
            msg = tlang(m, "rules.priv_rules.turned_off").format(chat_name=m.chat.title)
        else:
            msg = tlang(m, "rules.priv_rules.no_option")
        await m.reply_text(msg)
    elif len(m.text.split()) == 1:
        curr_pref = db.get_privrules()
        msg = tlang(m, "rules.priv_rules.current_preference").format(
            current_option=curr_pref,
        )
        LOGGER.info(f"{m.from_user.id} fetched privaterules preference in {m.chat.id}")
        await m.reply_text(msg)
    else:
        await m.reply_text(tlang(m, "general.check_help"))

    return


@Bot.on_message(filters.command("clearrules") & admin_filter)
async def clear_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    rules = db.get_rules()
    if not rules:
        await m.reply_text(tlang(m, "rules.no_rules"))
        return

    await m.reply_text(
        (tlang(m, "rules.clear_rules")),
        reply_markup=ikb(
            [[("⚠️ Confirm", "clear_rules"), ("❌ Cancel", "close_admin")]],
        ),
    )
    return


@Bot.on_callback_query(filters.regex("^clear_rules$"))
async def clearrules_callback(_, q: CallbackQuery):
    Rules(q.message.chat.id).clear_rules()
    await q.message.edit_text(tlang(q, "rules.cleared"))
    LOGGER.info(f"{q.from_user.id} cleared rules in {q.message.chat.id}")
    await q.answer("Rules for the chat have been cleared!", show_alert=True)
    return


__PLUGIN__ = "rules"

__alt_name__ = ["rule"]
