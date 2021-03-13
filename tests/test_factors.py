import unittest

from core_cs.problems.factors import get_factors


class MyTestCase(unittest.TestCase):
    def test_factors(self):
        f = get_factors(12)
        self.assertIs(type(f), list)
        self.assertEqual(f, [2, 3, 4, 6])
