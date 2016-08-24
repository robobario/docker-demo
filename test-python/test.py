import unittest
import requests
import time

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        time.sleep(3)
        r = requests.get('http://hello.world:8000')
        self.assertEqual(r.text, 'Hello, world')

if __name__ == '__main__':
    unittest.main()


