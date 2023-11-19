""" MQTT publisher """

import random
import time
import json
import paho.mqtt.client as mqtt

THE_BROKER = "mqtt"
THE_TOPIC = "charger/1/connector/1/session/1"

# Callback function used when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
    print("Connected!")

# Callback function used when a message is published.
def on_publish(client, userdata, mid):
    print("msg published (mid={})".format(mid))

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(THE_BROKER, port=1883, keepalive=60)
    client.loop_start()

    while True:
        data = {
            'session_id': 1,
            'energy_delivered_in_kWh': random.randint(0, 100),
            'duration_in_seconds': random.randint(0, 100),
            'session_cost_in_cents': random.randint(0, 100)
        }
        print("publishing: ", json.dumps(data))
        client.publish(THE_TOPIC, payload=json.dumps(data), qos=0, retain=False)
        time.sleep(5)

    client.loop_stop()