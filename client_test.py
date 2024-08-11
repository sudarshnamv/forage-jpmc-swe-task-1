import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint(self):
        quote = {'stock': 'ABC', 'top_bid': {'price': 120.48}, 'top_ask': {'price': 121.20}}
        expected = ('ABC', 120.48, 121.20, (120.48 + 121.20) / 2)
        self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio(self):
        self.assertEqual(getRatio(120, 60), 2)
        self.assertEqual(getRatio(120, 0), None)  # Check division by zero

if __name__ == "__main__":
    unittest.main()
