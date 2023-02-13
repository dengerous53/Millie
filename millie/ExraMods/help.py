import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from millie.misc import BUTTON_1
from Script import script

@Client.on_message(filters.command("help"))
async def helpless(_, message):
    the_real_message = "hear is my help command"
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = BUTTON_1
        await message.reply_text(f"{the_real_message}", reply_markup=pk, quote=True)
    except Exception as e:
        with open("help.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = BUTTON_1
        await message.reply_document(
            document="help.text",
            caption="hear is my help command",
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("help.text")


