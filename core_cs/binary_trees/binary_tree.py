class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinaryTree:
    """ This Binary Tree is made under the assumption that we are only handling integers with it. """
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def search(self, value):
        if self.root:
            return self._search(self.root, value)

    def _search(self, node, value):
        if node:
            if node.value == value:
                return node
            elif value > node.value:
                return self._search(node.right, value)
            elif value < node.value:
                return self._search(node.left, value)

    def min(self, node):
        if node.left:
            return self.min(node.left)
        else:
            return node

    def max(self, node):
        if node.right:
            return self.max(node.right)
        else:
            return node

    def delete(self, node):
        pass

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value, node)
        else:
            if node.right:
                self._add(node.right, value)
            else:
                node.right = Node(value, node)

    def successor(self, node):
        """
        There are two cases.
        Another way is to have an array with the in order traversal of the tree and get the value
        right after it.
        """
        # The first case is where the node has a right node.
        if node.right:
            return self.min(node.right)

        # The second case is when it doesnt have a right node.
        # Travel up using the parent pointer until you see a node which is
        # left child of it’s parent. The parent of such a node is the succesor.
        temp_node = node
        parent = node.parent
        while parent is not None and node == parent.left:
            if temp_node != parent.right:
                break
            temp_node = parent
            parent = parent.parent
        return parent

    def predecessor(self, node):
        """
        There are two cases.
        The first one is where the node has a left node.
        The other is when it doesnt. In this case it has to go up until it gets to the previous value.

        Another way is to have an array with the in order traversal of the tree and get the value
        right before it.
        """
        if node.left:
            return self.max(node.left)

        temp_node = node
        parent = node.parent
        while parent is not None and temp_node == parent.right:
            temp_node = parent
            parent = parent.parent

        return parent

    def inOrder(self):
        if self.root:
            self._inOrder(self.root)

    def _inOrder(self, node):
        if node:
            self._inOrder(node.left)
            print(node.value)
            self._inOrder(node.right)

    def preOrder(self):
        if self.root:
            self._preOrder(self.root)

    def _preOrder(self, node):
        if node:
            print(node.value)
            self._preOrder(node.left)
            self._preOrder(node.right)

    def postOrder(self):
        if self.root:
            self._postOrder(self.root)

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.value)

    def delete(self):
        pass

    def height(self):
        return self._height(self.get_root())

    def _height(self, node):
        if not node:
            return 0

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return max(left_height, right_height) + 1


if __name__ == "__main__":
    values = [5, 8, 9, 2, 1, 3, 4]
    bt = BinaryTree()
    for value in values:
        bt.add(value)
    temp_node2 = bt.search(2)
    s = bt.successor(temp_node2)
    print(s.value)
    print(bt.height())
