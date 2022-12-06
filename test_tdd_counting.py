import math
import unittest
from main import counting

class TestCounting(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(counting(0, 0, 0), [])
        self.assertEqual(counting(1,1,1),[])
        self.assertEqual(counting(2, -10, 2), [-2.1889010593167337, 2.1889010593167337,-0.45685025174785676,0.45685025174785676])
        self.assertEqual(counting(0, 1, 1), [-1.0, 1.0])
        self.assertEqual(counting(10, 100, 1000), [])
        self.assertEqual(counting(1, 0, 0), [-0.0])


if __name__ == '__main__':

    unittest.main()


