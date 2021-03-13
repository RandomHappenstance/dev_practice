import unittest

from core_cs.recursion.recursion import recursive_string_reverse, reverse_in_place
from helpers.string_helpers import generate_str, generate_list


class MyTestCase(unittest.TestCase):
    def test_recursive_string_reverse(self):
        word, word_reversed = generate_str()
        output = recursive_string_reverse(word)

        self.assertEqual(output, word_reversed)

    def test_reverse_in_place(self):
        word, word_reversed = generate_list()
        output = reverse_in_place(word)

        self.assertEqual(output, word_reversed)
        self.assertEqual(id(output), id(word))
