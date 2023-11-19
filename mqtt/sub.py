""" MQTT subscriber """

import logging
import paho.mqtt.client as mqtt

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
f_handler = logging.FileHandler('./log/sub.log', mode='w')
f_format = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

THE_BROKER = "mqtt"
THE_TOPIC = "charger/1/connector/1/session/1"

# Callback function used when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
    logger.info("Connected!")
    client.subscribe(THE_TOPIC, qos=0)

# Callback function used when the client receives a message from the broker.
def on_message(client, userdata, msg):
    msg = "Message received with topic: {} and payload: {}".format(msg.topic, str(msg.payload))
    logger.info(msg)
    # print(msg)

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(THE_BROKER, port=1883, keepalive=60)
    client.loop_forever()
