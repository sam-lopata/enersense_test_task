"""
Class to interact with mongodb
"""
from datetime import datetime
import paho.mqtt.client as mqtt
import pymongo
import pymongo.database
import pymongo.collection
import pymongo.errors

# mongodb://user:pass@ip:port || mongodb://ip:port
MONGO_URI = "mongodb://root:password@mongo:27017"
MONGO_DB = "enersense_db"
MONGO_COLLECTION = "sessions"
MONGO_TIMEOUT = 1  # Time in seconds
MONGO_DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"


class Mongo(object):
    def __init__(self):
        self.client: pymongo.MongoClient = None
        self.database: pymongo.database.Database = None
        self.collection: pymongo.collection.Collection = None

    def connect(self):
        print("Connecting Mongo")
        self.client = pymongo.MongoClient(
            MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT*1000.0)
        self.database = self.client.get_database(MONGO_DB)
        self.collection = self.database.get_collection(MONGO_COLLECTION)

    def disconnect(self):
        print("Disconnecting Mongo")
        if self.client:
            self.client.close()
            self.client = None

    def connected(self) -> bool:
        if not self.client:
            return False
        try:
            self.client.admin.command("ismaster")
        except pymongo.errors.PyMongoError:
            return False
        else:
            return True

    def save_one(self, msg: mqtt.MQTTMessage):
        now = datetime.now()
        try:
            document={
                "timestamp":int(now.timestamp()),
                "topic":msg.topic,
                "payload":msg.payload.decode(),
            }
            result = self.collection.insert_one(document)
            print("Saved in Mongo document ID", result.inserted_id)
        except Exception as ex:
            print(ex)
