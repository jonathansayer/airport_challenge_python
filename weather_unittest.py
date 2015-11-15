import unittest
from mock import Mock
import random
from weather import Weather

class WeatherTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_nice_weather(self):
        weather = Weather()
        random.seed(79)
        self.assertEqual(weather.stormy(),False)



if __name__ == '__main__':
    unittest.main()
