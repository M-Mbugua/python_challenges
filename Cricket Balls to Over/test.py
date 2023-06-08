import unittest
from total_overs import total_overs


class TotalOvers (unittest.TestCase):

    def total_overs(self):
        self.assert_equals(total_overs(2400), 400)
        self.assert_equals(total_overs(164), 27.2)
        self.assert_equals(total_overs(945), 157.3)
        self.assert_equals(total_overs(5), 0.5)
        self.assert_equals(total_overs(7), 1.1)
        self.assert_equals(total_overs(15), 2.3)
        self.assert_equals(total_overs(0), 0)
