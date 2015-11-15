import unittest
from mock import Mock
import random
from weather import Weather

class WeatherTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_nice_weather(self):
        weather = Weather()
        if weather.generator() <= 80:
            self.assertEqual(weather.stormy(), False)
        elif weather.generator() > 80:
            self.assertEqual(weather.stormy(),True)


if __name__ == '__main__':
    unittest.main()
