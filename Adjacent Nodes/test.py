import unittest
from adjacent_nodes import is_adjacent


class IsAdjacent (unittest.TestCase):
    AssertTrue = bool
    AssertFalse = bool

    def test_is_adjacent_true(self):
        matrix1 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        matrix2 = [[0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
        self.AssertTrue(is_adjacent(matrix1, 0, 1))
        self.AssertTrue(is_adjacent(matrix1, 2, 1))
        self.AssertTrue(is_adjacent(matrix2, 0, 1))
        self.AssertTrue(is_adjacent(matrix2, 2, 1))

    def test_is_adjacent_false(self):
        matrix1 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        matrix2 = [[0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
        self.AssertFalse(is_adjacent(matrix1, 0, 2))
        self.AssertFalse(is_adjacent(matrix2, 1, 4))

