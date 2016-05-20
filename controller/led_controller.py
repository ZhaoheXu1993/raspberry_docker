# encoding=utf-8
from __future__ import unicode_literals
import requests
import time


class LEDController(object):
    @staticmethod
    def led_blink():
        for i in xrange(2):
            try:
                requests.get('http://ylcktest.ngrok.cc/led/switch/open')
            except IOError:
                print Exception.message
            time.sleep(0.01)
            try:
                requests.get('http://ylcktest.ngrok.cc/led/switch/close')
            except IOError:
                print Exception.message
            time.sleep(0.01)
