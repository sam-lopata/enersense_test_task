# simulator device 1 for mqtt message publishing
import time
import random
import paho.mqtt.client as paho

# hostname
broker = "localhost"
# port
port = 1883


def on_publish(client, userdata, result):
    print("Device 1 : Data published.")
    pass


client = paho.Client("admin")
client.on_publish = on_publish
client.connect(broker, port)

d = random.randint(1, 50)

# telemetry to send
message = "Device 1 : Data " + str(d)
time.sleep(1)

# publish message
ret = client.publish("/data", message)

print("Stopped...")
