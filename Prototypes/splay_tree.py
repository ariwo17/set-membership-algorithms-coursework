class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SplayTreeSet():
    def __init__(self):
        self.root = None

    def searchElement(self, value):
        self.root = self.splay(self.root, value)
        if self.root is None or self.root.value != value:
            return False
        return True

    def insertElement(self, value):
        if self.root is None:
            self.root = Node(value)
            return True

        self.root = self.splay(self.root, value)
        if self.root.value == value:
            return False

        new_node = Node(value)
        if value < self.root.value:
            new_node.left = self.root.left
            new_node.right = self.root
            self.root.left = None
        else:
            new_node.right = self.root.right
            new_node.left = self.root
            self.root.right = None
        self.root = new_node
        return True

    def splay(self, root, value):
        if root is None or root.value == value:
            return root

        if value < root.value:
            if root.left is None:
                return root
            if value < root.left.value:
                root.left.left = self.splay(root.left.left, value)
                root = self.right_rotate(root)
            elif value > root.left.value:
                root.left.right = self.splay(root.left.right, value)
                if root.left.right is not None:
                    root.left = self.left_rotate(root.left)
            if root.left is not None:
                root = self.right_rotate(root)
            return root
        else:
            if root.right is None:
                return root
            if value < root.right.value:
                root.right.left = self.splay(root.right.left, value)
                if root.right.left is not None:
                    root.right = self.right_rotate(root.right)
            elif value > root.right.value:
                root.right.right = self.splay(root.right.right, value)
                root = self.left_rotate(root)
            if root.right is not None:
                root = self.left_rotate(root)
            return root

    def left_rotate(self, node):
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        return new_node

    def right_rotate(self, node):
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        return new_node