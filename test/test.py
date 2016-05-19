# encoding=utf-8
from __future__ import unicode_literals
import json
import unittest
from RaspBerry import *


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test(self):
        self.app.get('/')
