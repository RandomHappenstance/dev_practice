import unittest

from hackerrank.archived_problems.mult_3_5 import mult_sum


class EulerTestCases(unittest.TestCase):
    def test_prob_1(self):
        """ """

        sum = mult_sum(10)
        print(sum)
        self.assertEqual(sum, 23)

        sum = mult_sum(1000)
        print(sum)
        self.assertEqual(sum, 233168)
