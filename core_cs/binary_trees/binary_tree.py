class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """ This Binary Tree is made under the assumption that we are only handling integers with it. """
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def min(self, node):
        print(node.value)
        if node.left:
            return self.min(node.left)
        else:
            return node.value

    def max(self, node):
        print(node.value)
        if node.right:
            return self.max(node.right)
        else:
            return node.value

    def successor(self):
        pass

    def predecessor(self, node):
        pass

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(node.right, value)
            else:
                node.right = Node(value)

    def print_in_order(self):
        if self.root:
            self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(node.value)
            self._print_in_order(node.right)

    def print_pre_order(self):
        if self.root:
            self._print_pre_order(self.root)

    def _print_pre_order(self, node):
        if node:
            print(node.value)
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)

    def print_post_order(self):
        if self.root:
            self._print_post_order(self.root)

    def _print_post_order(self, node):
        if node:
            self._print_post_order(node.left)
            self._print_post_order(node.right)
            print(node.value)
