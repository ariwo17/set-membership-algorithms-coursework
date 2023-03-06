import timeit
import random


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key < key and self.left:
            return self.left.get(key)
        elif self.key > key and self.right:
            return self.right.get(key)
        else:
            return None

    def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
        else:
            self.right.put(key, value)

    def display(self, level=0):
        if self.right:
            self.right.display(level + 1)
        print('     ' * level, self.value)
        if self.left:
            self.left.display(level + 1)


class BST:
    def __init__(self, root):
        self.root = root

    def get(self, key):
        self.root.get(key)

    def put(self, key, value):
        self.root.put(key, value)

    def display(self):
        self.root.display()


root = Node(4, 4)
testBST = BST(root)
# root.left = Node(2, 2)
# root.right = Node(6, 6)
# root.left.left = Node(1, 1)
# root.left.right = Node(3, 3)
# root.right.left = Node(5, 5)
# root.right.right = Node(7, 7)

testBST.display()
