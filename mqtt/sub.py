import traceback
import sys
from mongo import Mongo
from logger import Logger
from mqtt import MQTT

mongo = Mongo()
logger = Logger()
mqtt = MQTT(mongo, logger)
mongo.connect()

try:
    mqtt.subscribe()
except Exception as e:
    traceback.print_exc()
    print('graceful_shutdown')
    mqtt.stop()
    sys.exit(0)
