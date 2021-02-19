import unittest
import pytest
# from binary_tree import BinaryTree
# from binary_tree import Node

from core_cs.binary_trees.binary_tree import BinaryTree
from core_cs.binary_trees.binary_tree import Node


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

    def test_get_min(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.min(bt.get_root()).value == 1

    def test_get_max(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.max(bt.get_root()).value == 9

    def test_successor(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.successor(bt.search(9)).value == None


class NodeTests(unittest.TestCase):

    def test_node_instantiation(self) -> None:
        node = Node(5, None)
        assert isinstance(node, Node)

    def test_node_instantiation_without_value(self):
        with pytest.raises(TypeError):
            node = Node()

    def test_node_attributes(self):
        node_attributes = ['left', 'parent', 'right', 'value']
        node = Node(0, None)
        self.assertEqual(sorted(list(node.__dict__.keys())), node_attributes)


if __name__ == '__main__':
    unittest.main()
