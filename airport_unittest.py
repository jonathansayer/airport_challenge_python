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
        airport.land_plane(plane)
        plane.land.assert_called_once_with()

    def test_airport_storing_planes(self):
        airport = Airport()
        plane = Mock()
        airport.land_plane(plane)
        self.assertEqual(airport.planes,[plane])

    def test_airport_take_off_plane(self):
        airport = Airport()
        plane = Mock()
        weather = Mock()
        weather.stormy.return_value = False
        airport.planes = [plane]
        airport.release_plane(plane,weather)
        plane.take_off.assert_called_once_with()

    def test_airport_release_plane(self):
        airport = Airport()
        plane = Mock()
        weather = Mock()
        weather.stormy.return_value = False
        airport.land_plane(plane)
        airport.release_plane(plane,weather)
        self.assertEqual(airport.planes,[])

    def test_stormy_weather(self):
        airport = Airport()
        plane = Mock()
        weather = Mock(stormy=True)
        airport.planes = [plane]
        self.assertEqual(airport.release_plane(plane,weather), "Weather is Stormy")


if __name__ == '__main__':
    unittest.main()
