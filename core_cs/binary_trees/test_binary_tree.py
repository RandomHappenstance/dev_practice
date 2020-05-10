import unittest
import pytest

from binary_tree import BinaryTree
from binary_tree import Node


class BinaryTreeTests(unittest.TestCase):

    def test_bt_instantiation(self):
        bt = BinaryTree()
        assert isinstance(bt, BinaryTree)


class NodeTests(unittest.TestCase):

    def test_node_instantiation(self) -> None:
        node = Node(5)
        assert isinstance(node, Node)

    def test_node_instantiation_without_value(self):
        with pytest.raises(TypeError):
            node = Node()

    def test_node_attributes(self):
        node_attributes = ['value', 'left', 'right']
        node = Node(0)
        self.assertEqual(list(node.__dict__.keys()), node_attributes)


if __name__ == '__main__':
    unittest.main()
