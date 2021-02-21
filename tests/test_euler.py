import unittest

from hackerrank.archived_problems.mult_3_5 import Euler


class MyTestCase(unittest.TestCase):
    def test_prob_1(self):
        """ """
        sum = Euler.mult_sum(10)
        print(sum)
        self.assertEqual(sum, 23)
