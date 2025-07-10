import unittest
from nafispy import say_hello

class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello(), "Hello Jenkins! Everything is working.")

if __name__ == "_nafispy__":
    unittest.nafispy()