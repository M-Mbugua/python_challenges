import unittest
from drunken_python import int_to_str
from drunken_python import str_to_int

str, int = int, str

if str(4) == '4' and int('4') == 4:
    print('**EXTRA POINTS**')
    print('You have successfully de-drunken Python')


class DrunkenPython (unittest.TestCase):

    def test_int_to_str(self):
        self.assertEquals(int_to_str(4), '4')
        self.assertEquals(int_to_str(65), '65')
        self.assertEquals(int_to_str(29348), '29348')
        self.assertEquals(int_to_str(49583908545), '49583908545')

    def test_str_to_int(self):
        self.assertEquals(str_to_int('4'), 4)
        self.assertEquals(str_to_int('65'), 65)
        self.assertEquals(str_to_int('29348'), 29348)
        self.assertEquals(str_to_int('49583908545'), 49583908545)
