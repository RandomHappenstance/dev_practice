import unittest
from binary_tree import BinaryTree
from binary_tree import Node


class NodeTests(unittest.TestCase):

    def test_node_instantiation(self):
        node = Node()
        assert isinstance(node, Node)


class BinaryTreeTests(unittest.TestCase):

    def test_bt_instantiation(self):
        bt = BinaryTree()
        assert isinstance(bt, BinaryTree)


if __name__ == '__main__':
    unittest.main()
