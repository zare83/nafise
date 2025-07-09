import unittest
from main import say_hello

class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello(), "Hello Jenkins! Everything is working.")

if __name__ == "__main__":
    unittest.main()