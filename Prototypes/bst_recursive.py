import timeit

SPACING_FACTOR = [10]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def get(self, value):
        return self._get(self.root, value)

    def _get(self, node, value):
        if node is None:
            return None
        elif value == node.value:
            return node.value
        elif value < node.value:
            return self._get(node.left, value)
        else:
            return self._get(node.right, value)

    def put(self, value):
        self.root = self._put(self.root, value)

    def _put(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._put(node.left, value)
        elif value > node.value:
            node.right = self._put(node.right, value)
        elif value == node.value:
            node.value = value
        return node

    def _display(self, root, space):
        if root is None:
            return
        space += SPACING_FACTOR[0]
        self._display(root.right, space)
        print()
        for i in range(SPACING_FACTOR[0], space):
            print(end=" ")
        print(root.value)
        self._display(root.left, space)

    def display(self):
        self._display(self.root, 0)


if __name__ == "__main__":
    testBST = BST()
    testBST.put("Hello")
    testBST.put("Shalom")
    testBST.put("Salaam")
    testBST.put("Hallo")
    testBST.put("Bonjour")
    testBST.put("Zdrasti")
    testBST.put("Buongiorno")
    testBST.display()

