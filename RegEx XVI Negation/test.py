import unittest
import re
from regex_negation import pattern

txt = ' alice15@gmail.com '


class RegexNegation(unittest.TestCase):
    def test_negation(self):
        self.assertEqual('[^' in pattern, True, 'You must use a negated character set in your expression.')
        self.assertEqual(re.findall(pattern, txt), ['@', '.'])

# Note from the original:
# Credits to https://javascript.info/regexp-character-sets-and-ranges

# Translated from JavaScript.
# The RegEx series was originally posted by Isaac Pak.