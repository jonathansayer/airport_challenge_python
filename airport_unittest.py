import unittest
from airport import Airport

class AirportTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_airport_capacity(self):
        airport = Airport()
        self.assertEqual(airport.capacity,20)


if __name__ == '__main__':
    unittest.main()
