import unittest

from core_cs.lists.add_two_numbers import add_two_numbers


class ListsTestCases(unittest.TestCase):
    def test_two_num(self):
        """ """
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]

        total = add_two_numbers(l1, l2)
        self.assertEqual(total, [7,0,8])

    def test_two_num_2(self):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        total = add_two_numbers(l1, l2)
        self.assertEqual(total, [8, 9, 9, 9, 0, 0, 0, 1])