import unittest
from plane import Plane

class PlaneTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_flying_when_initialized(self):
        plane = Plane()
        self.assertTrue(plane.flying)

    def test_not_flying_when_land(self):
        plane = Plane()
        plane.land()
        self.assertFalse(plane.flying)

    def test_flying_when_taking_off(self):
        plane = Plane()
        plane.flying = False
        plane.take_off()
        self.assertTrue(plane.flying)

if __name__ == '__main__':
    unittest.main()
