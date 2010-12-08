from __future__ import with_statement

import unittest
import datetime
import time
import random

from flask import Flask
from flaskext import {{extension.module_name}}

class {{extension.name}}TestCase(unittest.TestCase):
    
    def setUp(self):
        app = Flask(__name__)
        app.DEBUG = False
        app.TESTING = True
        self.app = app
        
    def tearDown(self):
        self.app = None