import unittest
from total_overs import total_overs


class TotalOvers (unittest.TestCase):
    def test_total_overs(self):
        self.assertEqual(total_overs(2400), 400)
        self.assertEqual(total_overs(164), 27.2)
        self.assertEqual(total_overs(945), 157.3)
        self.assertEqual(total_overs(5), 0.5)
        self.assertEqual(total_overs(7), 1.1)
        self.assertEqual(total_overs(15), 2.3)
        self.assertEqual(total_overs(0), 0)
