from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, WELCOM_PIC, WELCOM_TEXT, PICS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp
from Script import script
from pyrogram.errors import ChatAdminRequired
import random 

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(a=message.chat.title, b=message.chat.id, c=message.chat.username, d=total, e=r_j, f=temp.B_LINK))       
            await db.add_chat(message.chat.id, message.chat.title, message.chat.username)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from Indian HighCourt ന്റെ നിയമം പേടിച്ചു റിപ്പോയിലെ കോഡ് delete ആകിയവർ 
            buttons = [[
                InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NOT ALLOWED 🐞\n\n𝙼𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙷𝙰𝚂 𝚁𝙴𝚂𝚃𝚁𝙸𝙲𝚃𝙴𝙳 𝙼𝙴 𝙵𝚁𝙾𝙼 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙷𝙴𝚁𝙴 !𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙼𝙾𝚁𝙴 𝙰𝙱𝙾𝚄𝚃 𝙸𝚃 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙾𝚆𝙽𝙴𝚁...</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [
            [
                InlineKeyboardButton('𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴', url=f"https://t.me/{temp.U_NAME}?start=help")
            ]
            ]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>›› 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿.\n›› 𝙳𝙾𝙽'𝚃 𝙵𝙾𝚁𝙶𝙴𝚃 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.\n›› 𝙸𝚂 𝙰𝙽𝚈 𝙳𝙾𝚄𝙱𝚃𝚂 𝙰𝙱𝙾𝚄𝚃 𝚄𝚂𝙸𝙽𝙶 𝙼𝙴 𝙲𝙻𝙸𝙲𝙺 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽..⚡⚡.</b>",
            reply_markup=reply_markup)
    else:
        for u in message.new_chat_members:
            if (temp.MELCOW).get('welcome') is not None:
                try:
                    await (temp.MELCOW['welcome']).delete()
                except:
                    pass
            if WELCOM_PIC:
                temp.MELCOW['welcome'] = await message.reply_photo(photo=WELCOM_PIC, caption=WELCOM_TEXT.format(user=u.mention, chat=message.chat.title))
            else:
                temp.MELCOW['welcome'] = await message.reply_text(text=WELCOM_TEXT.format(user=u.mention, chat=message.chat.title))


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hello Friends, \nMy admin has told me to leave from group so i go! If you wanna add me again contact my support group.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat Not Found In DB")
    if cha_t['is_disabled']:
        return await message.reply(f"This chat is already disabled:\nReason-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Chat Succesfully Disabled')
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Hello Friends, \nMy admin has told me to leave from group so i go! If you wanna add me again contact my support group.</b> \nReason : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat Not Found In DB !")
    if not sts.get('is_disabled'):
        return await message.reply('This chat is not yet disabled.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat Succesfully re-enabled")


@Client.on_message(filters.command('paid_chat') & filters.user(ADMINS))
async def paid_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat Not Found In DB")
    if cha_t['is_paid']:
        return await message.reply(f"This chat is already disabled:\nReason-<code> {cha_t['reason']} </code>")
    await db.paid_chat(int(chat_), reason)
    temp.PRIM_CHATS.append(int(chat_))
    await message.reply('Chat Succesfully added to prime chat')
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Hello Friends, \nMy admin has told me to give this group prime access.</b> \nReason : <code>{reason}</code>',
            reply_markup=reply_markup)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('unpaid_chat') & filters.user(ADMINS))
async def re_paid_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat Not Found In DB !")
    if not sts.get('is_paid'):
        return await message.reply('This chat is not in prime list.')
    await db.re_paid_chat(int(chat_))
    temp.PRIM_CHATS.remove(int(chat_))
    await message.reply("Chat Succesfully add to free chat")

STATSBTN = [[
InlineKeyboardButton('𝚁𝙴𝙵𝚁𝙴𝚂𝙷', callback_data='statrfr')
        ]]


@Client.on_message(filters.command('stats'))
def statsmsg(client, message):
    message.reply_photo(
    photo=random.choice(PICS),
    caption = script.STATUS_TXT.format(temp.T_FILES, temp.T_USERS, temp.T_CHATS, temp.T_SIZE, temp.F_SIZE),
    reply_markup = InlineKeyboardMarkup(STATSBTN)
    )


# വാഴ മരത്തെ കളിയാക്കിയവർ തന്നെ പേടിച്ചു ഓടിപ്പോയി
@Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Invite Link Generation Failed, Iam Not Having Sufficient Rights")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')

@Client.on_message(filters.command('ban_user') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # വാഴ മരത്തെ കളിയാക്കിയവർ തന്നെ പേടിച്ചു ഓടിപ്പോയി
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is already banned\nReason: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Succesfully banned {k.mention}")


    
@Client.on_message(filters.command('unban_user') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("Thismight be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Succesfully unbanned {k.mention}")
        
        
@Client.on_message(filters.command('paid_user') & filters.user(ADMINS))
async def paid_a_user(bot, message):
    # വാഴ മരത്തെ കളിയാക്കിയവർ തന്നെ പേടിച്ചു ഓടിപ്പോയി
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_paid_status(k.id)
        if jar['is_paid']:
            return await message.reply(f"{k.mention} is already paid for me\nReason: {jar['paid_reason']}")
        await db.paid_user(k.id, reason)
        temp.PRIM_USERS.append(k.id)
        await message.reply(f"Succesfully add to prime user {k.mention}")


    
@Client.on_message(filters.command('unpaid_user') & filters.user(ADMINS))
async def unpaid_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("Thismight be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_paid_status(k.id)
        if not jar['is_paid']:
            return await message.reply(f"{k.mention} is not yet paid before.")
        await db.remove_paid(k.id)
        temp.PRIM_USERS.remove(k.id)
        await message.reply(f"Succesfully add to free user again {k.mention}")



    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # വാഴ മരത്തെ കളിയാക്കിയവർ തന്നെ പേടിച്ചു ഓടിപ്പോയി
    sps = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>\n"
    try:
        await sps.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('pusers') & filters.user(ADMINS))
async def plist_users(bot, message):
    sps = await message.reply('Getting List Of Users')
    users = temp.PRIM_USERS
    out = "Users Saved In DB Are:\n\n"
    out += f"<a href=tg://user?id={users['id']}>{users['name']}</a>\n<code>{users['id']}</code>\n"
    try:
        await sps.edit_text(out)
    except MessageTooLong:
        with open('pusers.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('pusers.txt', caption="List Of paid Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    sps = await message.reply('Getting List Of chats')
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    async for chat in chats:
        username = chat['username']
        username = "private" if not username else "@" + username
        out += f"**- Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`\n**Username:** {username}\n"
    try:
        await sps.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")





