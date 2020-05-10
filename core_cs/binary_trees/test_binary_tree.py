import unittest
import pytest

from binary_tree import BinaryTree
from binary_tree import Node


class BinaryTreeTests(unittest.TestCase):

    def test_instantiation(self):
        bt = BinaryTree()
        assert isinstance(bt, BinaryTree)

    def test_get_root(self):
        bt = BinaryTree()
        assert bt.get_root() == None

    def test_add_node(self):
        bt = BinaryTree()
        bt.add(5)
        assert bt.get_root().value == 5

    def test_insert_lower(self):
        bt = BinaryTree()
        bt.add(5)
        bt.add(3)
        assert bt.get_root().left.value == 3
        assert bt.get_root().right is None

    def test_insert_higher(self):
        bt = BinaryTree()
        bt.add(5)
        bt.add(8)
        assert bt.get_root().right.value == 8
        assert bt.get_root().left is None


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
