import os
import unittest
import tempfile
{% if app.layout=='factory' %}
import {{app.package_name}}
{% else %}
from app import app
{% endif %}

class {{app.package_name|title}}TestCase(unittest.TestCase):

    def setUp(self):
        {% if app.layout=='factory' %}
        self.app = {{app.package_name}}.create_app('Testing').test_client()
        {% else %}
        self.app = app.test_client()
        {% endif %}

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
