import json
import paho.mqtt.client as mqtt
from mongo import Mongo
from logger import Logger

MQTT_BROKER = "mqtt"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_QOS = 2
MQTT_TOPIC = "charger/1/connector/1/session/1"


class MQTT(object):
    def __init__(self, mongo: Mongo, logger: Logger):
        self.mongo: Mongo = mongo
        self.logger = logger
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_publish = self.on_publish

    # noinspection PyUnusedLocal
    @staticmethod
    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected MQTT")

    def on_publish(self, client, userdata, mid):
        print("msg published (mid=%s)", mid)

    # noinspection PyUnusedLocal
    def on_message(self, client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
        print("Recieved MQTT")
        self.logger.log(msg)
        self.mongo.save_one(msg)
        return msg

    def run(self):
        print("Running MQTT")
        self.mqtt_client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
        self.mqtt_client.loop_start()

    def stop(self):
        print("Stopping MQTT")
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

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
        subscirbe_result = self.mqtt_client.subscribe(MQTT_TOPIC, qos=0)
        print(subscirbe_result)
        self.mqtt_client.loop_forever()
