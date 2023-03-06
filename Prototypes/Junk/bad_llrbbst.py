SPACING_FACTOR = [10]
RED = True
BLACK = False


class Node:
    def __init__(self, value, colour=RED):
        self.value = value
        self.left = None
        self.right = None
        self.colour = colour


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

    def get(self, value):
        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node.value
        return None

    def put(self, value):
        node = self.root
        parent = None
        while node is not None:
            parent = node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                node.value = value
                return
        new_node = Node(value)
        if parent is None:
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self.balance(new_node)

    def balance(self, node):
        while self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        while self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        while self.is_red(node.left) and self.is_red(node.right):
            self.flip_colours(node)
            if node == self.root:
                node.colour = BLACK
            else:
                node = node.parent

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
    testBST.display()
