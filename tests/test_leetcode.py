import unittest
from leetcode.topics.recursion import recursive_string_reverse
from helpers.string_helpers import generate_str


class MyTestCase(unittest.TestCase):
    def test_recursive_string_reverse(self):
        word, word_reversed = generate_str()
        output = recursive_string_reverse(word)

        self.assertEqual(output, word_reversed)


if __name__ == '__main__':
    unittest.main()
