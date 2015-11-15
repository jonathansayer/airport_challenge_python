import unittest
from mock import Mock
from airport import Airport

class AirportTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_airport_capacity(self):
        airport = Airport()
        self.assertEqual(airport.capacity,20)

    def test_airport_land_plane(self):
        airport = Airport()
        plane = Mock()
        airport.land(plane)
        assetEqual(airport.planes,[plane])


if __name__ == '__main__':
    unittest.main()
