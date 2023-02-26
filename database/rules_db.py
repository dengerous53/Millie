from threading import RLock
from time import time

from pymongo import MongoClient
from pymongo.errors import PyMongoError

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

    def __init__(self, collection) -> None:
        self.collection = alita_main_db[collection]

    # Insert one entry into collection
    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return repr(result.inserted_id)

    # Find one entry from collection
    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            return result
        return False

    # Find entries from collection
    def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    # Count entries from collection
    def count(self, query=None):
        if query is None:
            query = {}
        return self.collection.count_documents(query)

    # Delete entry/entries from collection
    def delete_one(self, query):
        self.collection.delete_many(query)
        return self.collection.count_documents({})

    # Replace one entry in collection
    def replace(self, query, new_data):
        old = self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = self.collection.find_one({"_id": _id})
        return old, new

    # Update one entry from collection
    def update(self, query, update):
        result = self.collection.update_one(query, {"$set": update})
        new_document = self.collection.find_one(query)
        return result.modified_count, new_document

    @staticmethod
    def close():
        return alita_db_client.close()


def __connect_first():
    _ = MongoDB("test")
    LOGGER.info("Initialized Database!\n")


__connect_first()

INSERTION_LOCK = RLock()


class Rules(MongoDB):
    """Class for rules for chats in bot."""

    db_name = "rules"

    def __init__(self, chat_id: int) -> None:
        super().__init__(self.db_name)
        self.chat_id = chat_id
        self.chat_info = self.__ensure_in_db()

    def get_rules(self):
        with INSERTION_LOCK:
            return self.chat_info["rules"]

    def set_rules(self, rules: str):
        with INSERTION_LOCK:
            self.chat_info["rules"] = rules
            self.update({"_id": self.chat_id}, {"rules": rules})

    def get_privrules(self):
        with INSERTION_LOCK:
            return self.chat_info["privrules"]

    def set_privrules(self, privrules: bool):
        with INSERTION_LOCK:
            self.chat_info["privrules"] = privrules
            self.update({"_id": self.chat_id}, {"privrules": privrules})

    def clear_rules(self):
        with INSERTION_LOCK:
            return self.delete_one({"_id": self.chat_id})

    @staticmethod
    def count_chats_with_rules():
        with INSERTION_LOCK:
            collection = MongoDB(Rules.db_name)
            return collection.count({"rules": {"$regex": ".*"}})

    @staticmethod
    def count_privrules_chats():
        with INSERTION_LOCK:
            collection = MongoDB(Rules.db_name)
            return collection.count({"privrules": True})

    @staticmethod
    def count_grouprules_chats():
        with INSERTION_LOCK:
            collection = MongoDB(Rules.db_name)
            return collection.count({"privrules": False})

    @staticmethod
    def load_from_db():
        with INSERTION_LOCK:
            collection = MongoDB(Rules.db_name)
            return collection.find_all()

    def __ensure_in_db(self):
        chat_data = self.find_one({"_id": self.chat_id})
        if not chat_data:
            new_data = {"_id": self.chat_id, "privrules": False, "rules": ""}
            self.insert_one(new_data)
            LOGGER.info(f"Initialized Language Document for chat {self.chat_id}")
            return new_data
        return chat_data

    # Migrate if chat id changes!
    def migrate_chat(self, new_chat_id: int):
        old_chat_db = self.find_one({"_id": self.chat_id})
        new_data = old_chat_db.update({"_id": new_chat_id})
        self.insert_one(new_data)
        self.delete_one({"_id": self.chat_id})

    @staticmethod
    def repair_db(collection):
        all_data = collection.find_all()
        keys = {"privrules": False, "rules": ""}
        for data in all_data:
            for key, val in keys.items():
                try:
                    _ = data[key]
                except KeyError:
                    LOGGER.warning(
                        f"Repairing Rules Database - setting '{key}:{val}' for {data['_id']}",
                    )
                    collection.update({"_id": data["_id"]}, {key: val})


def __pre_req_all_rules():
    start = time()
    LOGGER.info("Starting Rules Database Repair...")
    collection = MongoDB(Rules.db_name)
    Rules.repair_db(collection)
    LOGGER.info(f"Done in {round((time() - start), 3)}s!")
