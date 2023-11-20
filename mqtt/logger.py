"""
Logger class
Writes logs with file handler to specified log file
Only logic for subscriber messages is impklemented
"""
import logging
import paho.mqtt.client as mqtt

class Logger(object):
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        f_handler = logging.FileHandler(log_file, mode='a+')
        f_format = logging.Formatter(
            '%(asctime)s  - %(levelname)s - %(message)s')
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(f_format)
        self.logger.addHandler(f_handler)

    def log_subscriber(self, msg: mqtt.MQTTMessage):
        self.logger.info(
            "Message received with topic: '%s' and payload: '%s'", msg.topic, str(msg.payload))

    def stop(self):
        handlers = self.logger.handlers[:]
        for handler in handlers:
            self.logger.removeHandler(handler)
            handler.close()
