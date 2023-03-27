import telebot
import re
from info import *
# Initialize the bot with your bot token
bot = telebot.TeleBot(BOT_TOKEN)

# Load custom filters from file
with open('filters.txt', 'r') as f:
    custom_filters = [line.strip() for line in f]

# Define the message handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message matches any of the custom filters
    for filter in custom_filters:
        if re.search(filter, message.text, re.IGNORECASE):
            bot.delete_message(message.chat.id, message.message_id)
            break

# Define the command handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the filter bot! Send me any message and I'll check if it matches any of the filters.")

# Define the command handler for /import command
@bot.message_handler(commands=['import'])
def import_filters(message):
    # Check if the user is an admin of the group
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    if not chat_member.status in ['administrator', 'creator']:
        bot.reply_to(message, "Only group admins can import filters.")
        return

    # Check if a file is attached to the message
    if not message.document:
        bot.reply_to(message, "Please attach a text file with the filters to import.")
        return

    # Download the file
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Decode the file contents and add filters to the list
    filters = downloaded_file.decode('utf-8').split('\n')
    filters = [filter.strip() for filter in filters if filter.strip()]
    custom_filters.extend(filters)

    # Save the updated filters to file
    with open('filters.txt', 'w') as f:
        f.write('\n'.join(custom_filters))

    bot.reply_to(message, f"{len(filters)} filters imported.")

# Define the command handler for /export command
@bot.message_handler(commands=['export'])
def export_filters(message):
    # Check if the user is an admin of the group
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    if not chat_member.status in ['administrator', 'creator']:
        bot.reply_to(message, "Only group admins can export filters.")
        return

    # Save the filters to a text file and send it to the user
    with open('filters.txt', 'r') as f:
        filters_file = telebot.types.InputFile('filters.txt', f.read())
    bot.send_document(message.chat.id, filters_file, caption="Here are the current filters in the group.")

# Start the bot
bot.polling()
