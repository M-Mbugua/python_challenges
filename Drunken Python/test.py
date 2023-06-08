import unittest
from drunken_python import int_to_str
from drunken_python import str_to_int

str, int = int, str

if str(4) == '4' and int('4') == 4:
    print('**EXTRA POINTS**')
    print('You have successfully de-drunken Python')


class DrunkenPython (unittest.TestCase):

    def int_to_str(self):
        self.assert_equals(int_to_str(4), '4')
        self.assert_equals(int_to_str(65), '65')
        self.assert_equals(int_to_str(29348), '29348')
        self.assert_equals(int_to_str(49583908545), '49583908545')

    def str_to_int(self):
        self.assert_equals(str_to_int('4'), 4)
        self.assert_equals(str_to_int('65'), 65)
        self.assert_equals(str_to_int('29348'), 29348)
        self.assert_equals(str_to_int('49583908545'), 49583908545)
