"""
MQTT subscriber
"""

import traceback
import sys
from mongo import Mongo
from logger import Logger
from mqtt import MQTT

LOG_FILE = './log/sub.log'

mongo = Mongo()
logger = Logger(LOG_FILE)
mqtt = MQTT(mongo, logger)
mongo.connect()

try:
    mqtt.subscribe()
except Exception as e:
    traceback.print_exc()
    print('graceful_shutdown')
    mqtt.stop()
    sys.exit(0)
