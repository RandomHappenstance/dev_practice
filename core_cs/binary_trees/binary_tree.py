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

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is not None:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else :
            if node.right is not None:
                self._add(node.right, value)
            else:
                node.right = Node(value)
