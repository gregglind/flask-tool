import os
import unittest
import tempfile
import {{app.package_name}}

class {{app.package_name|title}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{app.package_name}}.create_app('Testing').test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
