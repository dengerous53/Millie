# Kanged From https://github.com/KDBotz/LUCIFER

import pymongo
from info import DATABASE_URI, DATABASE_NAME
from pyrogram import enums
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient["Rules"]



async def add_rule(rules, text, reply_text, btn, file, alert):
    mycol = mydb[str(rules)]
    mycol.create_index([('text', 'text')])

    data = {
        'text':str(text),
        'reply':str(reply_text),
        'btn':str(btn),
        'file':str(file),
        'alert':str(alert)
    }

    try:
        mycol.update_one({'text': str(text)},  {"$set": data}, upsert=True)
    except:
        logger.exception('Some error occured!', exc_info=True)
             
     
async def find_rules(rules, name):
    mycol = mydb[str(rules)]
    
    query = mycol.find( {"text":name})
    query = mycol.find( { "$text": {"$search": name}})
    try:
        for file in query:
            reply_text = file['reply']
            btn = file['btn']
            fileid = file['file']
            try:
                alert = file['alert']
            except:
                alert = None
        return reply_text, btn, alert, fileid
    except:
        return None, None, None, None


async def get_rules(rules):
    mycol = mydb[str(rules)]

    texts = []
    query = mycol.find()
    try:
        for file in query:
            text = file['text']
            texts.append(text)
    except:
        pass
    return texts


async def delete_rules(message, text, rules):
    mycol = mydb[str(rules)]
    
    texts = []

    query = mycol.drop()
        await message.reply_text(
            f"'`{text}`'  deleted. I'll not respond to that rule anymore.",
            quote=True,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("Couldn't find that rule!", quote=True)

async def del_allrules(message, reply_text):
    if str(group_id) not in mydb.list_collection_names():
        await message.edit_text(f"Nothing to remove in {title}!")
        return

    mycol = mydb[str(reply_text)]
    try:
        mycol.drop()
        await message.edit_text(f"All rules from {title} has been removed")
    except:
        await message.edit_text("Couldn't remove all rules from group!")
        return

async def count_rules(reply_text):
    mycol = mydb[str(reply_text)]

    count = mycol.count()
    return False if count == 0 else count


async def rule_stats():
    collections = mydb.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    totalcount = 0
    for collection in collections:
        mycol = mydb[collection]
        count = mycol.count()
        totalcount += count

    totalcollections = len(collections)

    return totalcollections, totalcount
