import unittest
from binary_tree import BinaryTree as BT


class BinaryTreeTests(unittest.TestCase):

    def test_bt_instantiation(self):
        bt = BT()
        assert isinstance(bt, BT)


if __name__ == '__main__':
    unittest.main()
