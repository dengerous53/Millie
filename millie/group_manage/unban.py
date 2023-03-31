from pyrogram import Client, filters
from millie.helper.admin_check import admin_check
from millie.helper.extract import extract_time, extract_user                               
from utils import temp 
from info import LOG_CHANNEL

@Client.on_message(filters.command(["unban", "unmute"]))
async def un_ban_user(bot, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.unban_member(user_id=user_id)
        await bot.send_message(LOG_CHANNEL, text=f"**UNBAN**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: UNBANNED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay, changed ... now "
                f"{user_first_name} To "
                " You can join the group!"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**UNMUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: UNMUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        else:
            await message.reply_text(
                "Okay, changed ... now "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                " You can join the group!"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**UNMUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: UNMUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        
