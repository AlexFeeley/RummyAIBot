# I just filled out a little bit of how to write tests to use to test the script to compile all
# tests. You can look at my deck test to see how to write them or google it. I just needed to use
# this to test the script

import unittest

class TestDeck(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
