import unittest

from hackerrank.archived_problems.mult_3_5 import mult_sum


class EulerTestCases(unittest.TestCase):
    def test_prob_1(self):
        """ """

        total = mult_sum(10)
        self.assertEqual(total, 23)

        total = mult_sum(1000)
        self.assertEqual(total, 233168)
