class script(object):   
    HELP_TXT = """𝙷𝙴𝚈 {}\n𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴 : {}
✯ 𝙳𝙰𝙳𝙳𝚈 : <a href=https://t.me/renish_rgi>❁✗❍═❰ RENISH ❱═❍✗❁</a>
✯ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝚒𝚍 : <a href=https://t.me/Millie_support>Millie Support</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙰𝙽𝚈𝚆𝙷𝙴𝚁𝙴
✯ 𝙱𝚄𝙸𝙻𝙳 𝚅𝙴𝚁𝚂𝙸𝙾𝙽: 𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁-𝙱𝙾𝚃 𝚟3.0.0"""

    YOUTUBE_TXT = """ ⭐⭐ NEW UPDATE ⭐⭐
Download video
Download song
Download shorts
From YouTube using this bot
Command.  /video , /mp4 , /vsonng , /yt , /ytdl , /short , /shorts for video
/audio , /mp3 , /asong , /song , /ayt , /aytdl , /ashort , /ashorts for audio
EXAMPLE & more information
is on video & audio buttons """

    AUDIO_TXT = """⭐⭐⭐ NEW UPDATE ⭐⭐⭐
Download audio song from YouTube
You can download shorts too

Use command
/audio , /mp3 , /asong , /song , /ayt , /aytdl , /ashort , /ashorts 

EXAMPLE :- 
1. /MP3 tum hi ho 
For search 
2. /MP3 https://youtu.be/Umqb9KENgmk
For using your link 
3. /MP3 https://youtube.com/shorts/ag84IxglCfY?feature=share
For shorts video
"""


    VIDEO_TXT = """⭐⭐⭐ NEW UPDATE ⭐⭐⭐
Download video song from YouTube
You can download shorts too

Use command
/video , /mp4 , /vsonng , /yt , /ytdl , /short , /shorts

EXAMPLE :- 
1. /MP4 tum hi ho 
For search 
2. /MP4 https://youtu.be/Umqb9KENgmk
For using your link 
3. /MP4 https://youtube.com/shorts/ag84IxglCfY?feature=share
For shorts video
"""

    SOURCE_TXT = """<b>NOTE:</b>
Click 👇👇 source button for source 

<b>DEVS:</b>
✯ 𝙳𝙰𝙳𝙳𝚈 : <a href=https://t.me/renish_rgi>❁✗❍═❰ RENISH ❱═❍✗❁</a>
✯ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝚒𝚍 : <a href=https://t.me/Millie_support>Millie Support</a>
"""
    
    REPORT_TXT = """👉 HELP For REPORT 🚨

This command helps you to report a message or a user to admins on the respective group.

Don't misuse this command
Otherwise you will block
Or ban from group & admin

⭐⭐ Command ⭐⭐
/Report
@admin
@admins
⭐⭐ Example to use ⭐⭐

👉 /Report  - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""
    
    AFK_TXT = """
❤️‍🔥❤️‍🔥NEW update ❤️‍🔥❤️‍🔥
AFK
When someone mentions you in a chat, 
the user will be notified you are AFK. 
You can even provide a reason for going AFK,
which will be provided to the user as well.

- `/afk` - This will set you offline.
- `/afk [Reason]` - This will set you offline with a reason.
- `/afk [Replied to a Sticker/Photo]` - This will set you offline with an image or sticker.
- `/afk [Replied to a Sticker/Photo] [Reason]` - This will set you afk with an image and reason both.
"""

    RULES_TXT = """
Coming soon....
XxxxxxxxxxxxxxxxxxxxxxX
Every chat works with different rules; this module will help make those rules clearer!

**User commands:**
- /rules: Check the current chat rules.

**Admin commands:**
- /setrules `<text>`: Set the rules for this chat. Supports markdown, buttons, fillings, etc.
- /privaterules `<yes/no/on/off>`: on|off whether the rules should be sent in private.
- /clearrules: Reset the chat rules to default.
"""

    NOTES_TXT = """
Coming soon....
XxxxxxxxxxxxxxxxxxxxxxX
Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!

**User commands:**
- /get `<notename>`: Get a note.
- #notename: Same as `/get`.

**Admin commands:**
- /save `<notename>` `<note text>`: Save a new note called "word". Replying to a message will save that message. Even works on media!
- /clear `<notename>`: Delete the associated note.
- /notes: List all notes in the current chat.
- /saved: Same as /notes.
- /clearall: Delete ALL notes in a chat. This cannot be undone.
"""

    LOCKS_TXT = """
❤️‍🔥❤️‍🔥NEW update ❤️‍🔥❤️‍🔥
**Locks**
Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!
The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!

**Admin commands:**
- /lock <item(s)>: Lock one or more items. Now, only admins can use this type!
- /unlock <item(s)>: Unlock one or more items. Everyone can use this type again!
- /locks: List currently locked items.
- /locktypes: Show the list of all lockable items.

**Examples:**
- Lock stickers with:
• `/lock sticker`
- You can lock/unlock multiple items by chaining them:
• `/lock sticker photo gif video`
"""

    CHATBOT_TXT = """
Coming soon....
XxxxxxxxxxxxxxxxxxxxxxX
**Chatbot**
AI based chatbot allows rose to talk and provides a more interactive group chat experience.
- /chatbot [ON/OFF]: Enables and disables Affiliate + AI Chat bot.
**Available chatbots**
• Luna - Advanced, inteligent and cute chatbot which will keep you happy all time.. 
**Language Support**
Rose AI chatbot support almost all languages in world .
"""

    FILE_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../

<b>𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺  𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝚆 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈  𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝙵𝙸𝙻𝙴𝚂...//</b>

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›

➪ /plink ›› <b>𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.</b>
➪ /pbatch ›› <b>𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙻𝙸𝙽𝙺 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>
➪ /batch ›› <b>𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙵𝙸𝙻𝙴𝚂.</b>

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

<code>/batch https://t.me/mkn_bots_updates https://t.me/mkn_bots_updates</code>

𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› <a href=https://t.me/mkn_bots_updates><b>𝙼𝙺𝙽 𝙱𝙾𝚃𝚉</b></a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>

• <code>/g_filter on</code> use this commoand + on/off in your group to control global filter in your group"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Millie](buttonurl:t.me/Millie_power_robot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙼𝙾𝙳𝚄𝙻𝙴..
<u>USE THIS COMMAND ON YOUR GROUP</u>
DISABLED FOR NOW
THIS will not work 
• /autofilter on - autofilter enable in yor chat
• /autofilter off - autofilter disable in your chat 

𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙰𝙽𝙳 𝚂𝙰𝚅𝙴  𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙵𝚁𝙾𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚃𝙾 𝙾𝙽 𝙰𝙽𝙳 𝙾𝙵𝙵 𝚃𝙷𝙴 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿../

𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 :-
›› /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁. 
›› /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.

𝙲𝚁𝙴𝙳𝙸𝚃𝚂 :-  <a href=https://t.me/millie_rmvzz>Millie Bobby brown</a>**"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔋 <u><b>Basic Command</b></u>
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>

🗂️ <u><b>Database & Server Command</b></u>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀᴛʙᴀꜱᴇ ꜱᴛᴀᴛᴜꜱ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>"""

    US_CHAT_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

📯 <u><b>Chat & User</b></u>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /restart - <code>Tᴏ Rᴇsᴛᴀʀᴛ ᴀ Bᴏᴛ</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>"""

    G_FIL_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔥 <u><b>Adv Global Filter </b></u>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ</code>
"""

    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚂𝙸𝚉𝙴: <code>512 MB</code></b>
<b>᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> </b>
<b>᚛› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> </b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
<b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>

By {f}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
<b>᚛› 𝐔𝐍 - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖻𝗒  <a href=https://t.me/millie_rmvzz>Millie Bobby brown</a>"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>

<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>

<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>

◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""

    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /ping - To get your ping.
<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me this command reply with Picture or Vide Under (5MB) 

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    CARB_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽︎
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""

    FOND_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗙𝗢𝗡𝗧𝗦☽︎
𝙵𝙾𝙽𝚃 𝙸𝚂 𝙰 𝙼𝙾𝙳𝚄𝙻𝙴 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝚂𝚃𝚈𝙻𝙸𝚂𝙷.
𝙵𝙾𝚁 𝚄𝚂𝙴 𝚃𝙷𝙰𝚃 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝚈𝙿𝙴 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""

    SHARE_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗦𝗛𝗔𝗥𝗘 𝗧𝗘𝗫𝗧☽︎

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
• /share - 𝚁𝚎𝚙𝚕𝚢 𝚆𝚒𝚝𝚑 𝙰𝚗𝚢 𝚃𝚎𝚡𝚝 𝚃𝚘 𝚂𝚎𝚗𝚍 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 """

    REQUEST_TXT = """<b>
🔥 HELP FOR REQUEST 🔥
🔥 MOVIES & SERIES 🔥

Command

/Req /request #request 

❤️How to request movie❤️
👉 You can send DM or you can send in group 
👉 You must type about your request [Minimum 3 Characters]. Requests can't be empty.

EXAMPLE

/Req pushpa
/Request pushpa
#request pushpa 

You can use any of above

🚨NOTE🚨

DON'T USE ALL OF ABOVE
</b>"""

    TRANSPARENT_TXT = """<b>
❤️‍🔥❤️‍🔥NEW UPDATE ❤️‍🔥❤️‍🔥
✅🔍 GOOGLE TRANSLATOR 🔍✅

Reply your massage with command
/tr <leng>
To translate your massage

EXAMPLE
X. If you want to translate in Hindi
Reply massage /tr hi
X. If you want to translate in English
Reply your massage /tr en
 </b>"""   

 
    ABOOK_TXT = """<b>
❤️‍🔥❤️‍🔥NEW UPDATE ❤️‍🔥❤️‍🔥
Fᴇᴀᴛᴜʀᴇs: Aᴜᴅɪᴏ Bᴏᴏᴋ
- ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴀ ᴘᴅғ ғɪʟᴇ ᴛᴏ ᴀ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /audiobook - ʀᴇᴘʟʏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀɴʏ ᴘᴅғ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ
</b>"""
    

    CORONA_TXT = """
❤️‍🔥❤️‍🔥NEW UPDATE ❤️‍🔥❤️‍🔥
➤ 𝐇𝐞𝐥𝐩: COVID - 19

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/covid 𝖨𝗇𝖽𝗂𝖺"""

    

