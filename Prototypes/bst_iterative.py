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
        current = self.root
        while current:
            if current.value == value:
                return current.value
            elif current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
        return None

    def put(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if current.value == value:
                    return
                elif current.value > value:
                    if not current.left:
                        current.left = Node(value)
                        return
                    current = current.left
                elif current.value < value:
                    if not current.right:
                        current.right = Node(value)
                        return
                    current = current.right

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

