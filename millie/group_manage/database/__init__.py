from pymongo import MongoClient
from pymongo.errors import PyMongoError
import asyncio
from info import DATABASE_NAME, DATABASE_URI, LOGGER

DB_NAME = DATABASE_NAME
DB_URI = DATABASE_URI

try:
    alita_db_client = MongoClient(DB_URI)
except PyMongoError as f:
    LOGGER.error(f"Error in Mongodb: {f}")
    exiter(1)
alita_main_db = alita_db_client[DB_NAME]


class MongoDB:
    """Class for interacting with Bot database."""

    async def __init__(self, collection) -> None:
        await self.collection == alita_main_db[collection]

    # Insert one entry into collection
    async def insert_one(self, document):
        result = await self.collection.insert_one(document)
        return repr(result.inserted_id)

    # Find one entry from collection
    async def find_one(self, query):
        result = await self.collection.find_one(query)
        if result:
            return result
        return False

    # Find entries from collection
    async def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    # Count entries from collection
    async def count(self, query=None):
        if query is None:
            query = {}
        return await self.collection.count_documents(query)

    # Delete entry/entries from collection
    async def delete_one(self, query):
        await self.collection.delete_many(query)
        return self.collection.count_documents({})

    # Replace one entry in collection
    async def replace(self, query, new_data):
        old = await self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = await self.collection.find_one({"_id": _id})
        return old, new

    # Update one entry from collection
    async def update(self, query, update):
        result = await self.collection.update_one(query, {"$set": update})
        new_document = await self.collection.find_one(query)
        return result.modified_count, new_document

    @staticmethod
    def close():
        return alita_db_client.close()


async def __connect_first():
    LOGGER.info("Initialized Database!\n")

asyncio.run(__connect_first())

