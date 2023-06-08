import unittest
from top_note import top_note


class TopNote (unittest.TestCase):
    def test_top_note(self):
        self.assertEqual(top_note({"name": "Jacek", "notes": [5, 4, 3]}), {"name": "Jacek", "top_note": 5})
        self.assertEqual(top_note({"name": "Ewa", "notes": [3, 3, 3]}), {"name": "Ewa", "top_note": 3})
        self.assertEqual(top_note({"name": "Zygmund", "notes": [1, 2, 3]}), {"name": "Zygmund", "top_note": 3})
        self.assertEqual(top_note({"name": "Alex", "notes": [1, 4, 6]}), {"name": "Alex", "top_note": 6})
