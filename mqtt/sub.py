""" MQTT subscriber """

import paho.mqtt.client as mqtt

THE_BROKER = "mqtt"
THE_TOPIC = "charger/1/connector/1/session/1"

# Callback function used when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
    print("connected to ", client._host, "port: ", client._port)
    print("flags: ", flags, "returned code: ", rc)
    client.subscribe(THE_TOPIC, qos=0)

# Callback function used when the client receives a message from the broker.
def on_message(client, userdata, msg):
    print("message received with topic: {} and payload: {}".format(
        msg.topic, str(msg.payload)))


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(THE_BROKER, port=1883, keepalive=60)
    client.loop_forever()
