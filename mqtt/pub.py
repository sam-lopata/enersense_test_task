"""
MQTT publisher
"""

import random
import time
import sys
import traceback
from mongo import Mongo
from logger import Logger
from mqtt import MQTT

mongo = Mongo()
logger = Logger()
mqtt = MQTT(mongo, logger)
mqtt.run()

try:
    while True:
        data = {
            'session_id': 1,
            'energy_delivered_in_kWh': random.randint(0, 100),
            'duration_in_seconds': random.randint(0, 100),
            'session_cost_in_cents': random.randint(0, 100)
        }
        mqtt.publish(data)
        time.sleep(5)
except Exception as e:
    traceback.print_exc()
    print('graceful_shutdown')
    mqtt.stop()
    sys.exit(0)
