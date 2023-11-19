import logging
import paho.mqtt.client as mqtt

LOG_FILE = './log/sub.log'

class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        f_handler = logging.FileHandler(LOG_FILE, mode='w')
        f_format = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(f_format)
        self.logger.addHandler(f_handler)
        
    def log(self, msg: mqtt.MQTTMessage):
        self.logger.info("Message received with topic: '%s' and payload: '%s'", msg.topic, str(msg.payload))