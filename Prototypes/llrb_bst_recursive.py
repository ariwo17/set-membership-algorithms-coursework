SPACING_FACTOR = [10]
RED = True
BLACK = False


class Node:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour
        self.left = None
        self.right = None


class LLRB_BST:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.colour == RED

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.colour = node.colour
        node.colour = RED
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.colour = node.colour
        node.colour = RED
        return x

    def flip_colours(self, node):
        node.colour = RED
        node.left.colour = BLACK
        node.right.colour = BLACK

    def put(self, value):
        self.root = self._put(self.root, value)
        self.root.colour = BLACK

    def _put(self, node, value):
        if node is None:
            return Node(value, RED)

        if value < node.value:
            node.left = self._put(node.left, value)
        elif value > node.value:
            node.right = self._put(node.right, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colours(node)

        return node

    def get(self, value):
        return self._get(self.root, value)

    def _get(self, node, value):
        if node is None:
            return None

        if value < node.value:
            return self._get(node.left, value)
        elif value > node.value:
            return self._get(node.right, value)
        else:
            return node.value

    def _display(self, root, space):
        if root is None:
            return
        space += SPACING_FACTOR[0]
        self._display(root.right, space)
        print()
        for i in range(SPACING_FACTOR[0], space):
            print(end=" ")
        if self.is_red(root):
            print(f'({root.value})')
        else:
            print(root.value)
        self._display(root.left, space)

    def display(self):
        self._display(self.root, 0)

if __name__ == "__main__":
    testBST = LLRB_BST()
    testBST.put("Hello")
    testBST.put("Shalom")
    testBST.put("Salaam")
    testBST.put("Hallo")
    testBST.put("Bonjour")
    testBST.put("Zdrasti")
    testBST.put("Buongiorno")
    testBST.put("Buongiraffe")
    testBST.put("Shelaam")
    testBST.put("Privet")
    testBST.display()
