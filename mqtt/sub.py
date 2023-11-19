#!/usr/bin/env python3

""" MQTT subscriber """

import logging
import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
f_handler = logging.FileHandler('./log/sub.log', mode='w')
f_format = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

# Set up client for MongoDB
mongo_client=MongoClient(host='mongo', port=27017, username="root", password="password")
db=mongo_client.enersense_db
collection=db.enersense_collection

THE_BROKER = "mqtt"
THE_TOPIC = "charger/1/connector/1/session/1"

# Callback function used when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
    logger.info("Connected!")
    client.subscribe(THE_TOPIC, qos=0)

# Callback function used when the client receives a message from the broker.
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    msg = "Message received with topic: {} and payload: {}".format(topic, str(payload))
    logger.info(msg)

    receive_time=datetime.datetime.now()
    post={"time":receive_time,"topic":topic,"value":str(payload)}
    collection.insert_one(post)
    # print(msg)

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(THE_BROKER, port=1883, keepalive=60)
    client.loop_forever()
