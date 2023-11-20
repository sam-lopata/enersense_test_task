"""
Class to interact with MQTT broker
On message recieve it writes it to log file and store in mongodb
"""
import uuid
import json
import paho.mqtt.client as mqtt
from mongo import Mongo
from logger import Logger

MQTT_BROKER = "mqtt"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 30
MQTT_QOS = 2
MQTT_TOPIC = "charger/1/connector/1/session/1"


class MQTT(object):
    def __init__(self, mongo: Mongo, logger: Logger):
        self.client_id = uuid.uuid4()
        self.mongo: Mongo = mongo
        self.logger = logger
        self.mqtt_client = mqtt.Client(self.client_id.hex, clean_session=False)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_publish = self.on_publish

    @staticmethod
    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected MQTT")

    def on_publish(self, client, userdata, mid):
        print("msg published (mid=%s)", mid)

    def on_message(self, client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
        print("Recieved MQTT")
        self.logger.log_subscriber(msg)
        self.mongo.save_one(msg)
        return msg

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected MQTT disconnection. Attempting to reconnect.")

    def run(self):
        print("Running MQTT")
        self.mqtt_client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
        self.mqtt_client.loop_start()

    def stop(self):
        print("Stopping MQTT")
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
        self.logger.stop()

    def publish(self, data: json):
        print("publishing: ", json.dumps(data))
        publish_result = self.mqtt_client.publish(
            MQTT_TOPIC, payload=json.dumps(data), qos=0, retain=False)
        publish_result.wait_for_publish()
        if publish_result.is_published():
            print("published")
        else:
            print("publish failed")

    def subscribe(self):
        print("Subscribing MQTT")
        self.mqtt_client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
        self.mqtt_client.subscribe(MQTT_TOPIC, qos=0)
        self.mqtt_client.loop_forever()
