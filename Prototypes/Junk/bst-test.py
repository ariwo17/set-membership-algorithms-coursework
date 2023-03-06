# class Node:
#     def __init__(self, key, value, left=None, right=None):
#         self.key = key
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def get(self, key):
#         current = self.root
#         while current:
#             if current.key == key:
#                 return current.value
#             elif current.key > key:
#                 current = current.left
#             else:
#                 current = current.right
#         return None
#
#     def put(self, key, value):
#         if not self.root:
#             self.root = Node(key, value)
#             return
#         current = self.root
#         while current:
#             if current.key == key:
#                 current.value = value
#                 return
#             elif current.key > key:
#                 if not current.left:
#                     current.left = Node(key, value)
#                     return
#                 current = current.left
#             else:
#                 if not current.right:
#                     current.right = Node(key, value)
#                     return
#                 current = current.right
#
#     def display(self):
#         def get_height(node):
#             if not node:
#                 return 0
#             left_height = get_height(node.left)
#             right_height = get_height(node.right)
#             return max(left_height, right_height) + 1
#
#         def print_node(node, level):
#             if not node:
#                 return
#             spaces = " " * (2 ** (max_level - level + 1) - 1)
#             print(spaces + f"{node.key}:{node.value}" + spaces, end="")
#
#         max_level = get_height(self.root)
#         nodes = [(self.root, 1)]
#         for level in range(1, max_level + 1):
#             line = ""
#             for node, node_level in nodes:
#                 if node_level == level:
#                     print_node(node, level)
#                     line += " " * (2 ** (max_level - level + 2) - 1)
#                 elif node_level == level + 1:
#                     line += " " * (2 ** (max_level - level + 1) - 1) + "/" + " " * (2 ** (max_level - level + 1) - 2)
#                     line += "\\" + " " * (2 ** (max_level - level + 1) - 1)
#                 else:
#                     line += " " * (2 ** (max_level - level + 2) - 1) * 2
#             print(line)
#             nodes = [(node.left, node_level + 1) for node, node_level in nodes if node] + [(node.right, node_level + 1)
#                                                                                            for node, node_level in nodes
#                                                                                            if node]
#
#
# bst = BST()
# bst.put(5, 5)
# bst.put(3, 3)
# bst.put(7, 7)
# bst.put(2, 2)
# bst.put(4, 4)
# bst.put(6, 6)
# bst.put(8, 8)
#
# print(bst.get(7))
#
# bst.display()
