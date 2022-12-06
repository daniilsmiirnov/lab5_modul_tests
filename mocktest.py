import unittest
from unittest.mock import Mock
from main import *
from unittest import TestCase
from unittest.mock import patch
# class Mock_counting(unittest.TestCase):
#
#     def test_counting(self):
#         mock = Mock(return_value=1)
#         counting(mock(), 1, 1)


class TestCost(TestCase):
    @patch('main.counting', return_value=[])
    def test_mock_counting(self,A):
        self.assertEqual(counting(1,1,1), [])

if __name__ == "__main__":
    unittest.main()
