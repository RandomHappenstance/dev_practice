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

    def test_add_lower(self):
        bt = BinaryTree()
        bt.add(5)
        bt.add(3)
        assert bt.get_root().left.value == 3
        assert bt.get_root().right is None

    def test_add_higher(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.get_root().right.value == 8
        assert bt.get_root().left.value == 2

    def test_print_in_order(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        bt.print_in_order()

    def test_print_pre_order(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        bt.print_pre_order()

    def test_print_post_order(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        bt.print_post_order()

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

    def test_search(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.search(5).value == 5
        assert bt.search(9).value == 9
        assert type(bt.search(9)) == Node

    def test_successor(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.successor(bt.search(2)).value == 3

    def test_predecessor(self):
        values = [5, 8, 9, 2, 1, 3]
        bt = BinaryTree()
        for value in values:
            bt.add(value)
        assert bt.predecessor(bt.search(5)).value == 3


class NodeTests(unittest.TestCase):

    def test_node_instantiation(self) -> None:
        node = Node(5)
        assert isinstance(node, Node)

    def test_node_instantiation_without_value(self):
        with pytest.raises(TypeError):
            node = Node()

    def test_node_attributes(self):
        node_attributes = ['value', 'left', 'right', 'parent']
        node = Node(0)
        self.assertEqual(list(node.__dict__.keys()), node_attributes)


if __name__ == '__main__':
    unittest.main()
