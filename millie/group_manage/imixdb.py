import telebot
import re
from info import *
# Initialize the bot with your bot token
bot = telebot.TeleBot(BOT_TOKEN)

def update_filters(update, context):
    open('filters.txt', 'w').close() # create/clear the file
    chat_id = update.message.chat_id
    filters = []
    with open('filters.txt', 'r') as f:
        for line in f:
            filters.append(line.strip())
    context.bot.send_message(chat_id=chat_id, text="Current filters:\n" + "\n".join(filters))

def add_filter(update, context):
    open('filters.txt', 'w').close() # create/clear the file
    chat_id = update.message.chat_id
    filter_text = update.message.text.replace("/add_filter ", "")
    with open('filters.txt', 'a') as f:
        f.write(filter_text + "\n")
    context.bot.send_message(chat_id=chat_id, text=f"Added filter: {filter_text}")

def delete_filter(update, context):
    open('filters.txt', 'w').close() # create/clear the file
    chat_id = update.message.chat_id
    filter_text = update.message.text.replace("/delete_filter ", "")
    filters = []
    with open('filters.txt', 'r') as f:
        for line in f:
            if line.strip() != filter_text:
                filters.append(line.strip())
    with open('filters.txt', 'w') as f:
        f.write("\n".join(filters))
    context.bot.send_message(chat_id=chat_id, text=f"Deleted filter: {filter_text}")

def import_filters(update, context):
    open('filters.txt', 'w').close() # create/clear the file
    chat_id = update.message.chat_id
    file = update.message.document
    if file.mime_type == 'text/plain':
        file_name = file.file_name or 'filters.txt'
        file.get_file().download(file_name)
        with open(file_name, 'r') as f:
            for line in f:
                context.bot_data.setdefault('filters', set()).add(line.strip())
        context.bot.send_message(chat_id=chat_id, text="Filters imported successfully!")
    else:
        context.bot.send_message(chat_id=chat_id, text="Please upload a text file.")

def export_filters(update, context):
    open('filters.txt', 'w').close() # create/clear the file
    chat_id = update.message.chat_id
    filters = context.bot_data.get('filters', set())
    if filters:
        with open('filters.txt', 'w') as f:
            f.write('\n'.join(filters))
        with open('filters.txt', 'rb') as f:
            context.bot.send_document(chat_id=chat_id, document=f, filename='filters.txt')
    else:
        context.bot.send_message(chat_id=chat_id, text="No filters to export.")

# Load custom filters from file

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
