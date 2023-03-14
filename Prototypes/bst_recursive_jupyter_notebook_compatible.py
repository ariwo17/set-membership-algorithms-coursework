# DO NOT MODIFY THIS CELL

from abc import ABC, abstractmethod


# abstract class to represent a set and its insert/search operations
class AbstractSet(ABC):

    # constructor
    @abstractmethod
    def __init__(self):
        pass

        # inserts "element" in the set

    # returns "True" after successful insertion, "False" if the element is already in the set
    # element : str
    # inserted : bool
    @abstractmethod
    def insertElement(self, element):
        inserted = False
        return inserted

        # checks whether "element" is in the set

    # returns "True" if it is, "False" otherwise
    # element : str
    # found : bool
    @abstractmethod
    def searchElement(self, element):
        found = False
        return found

    # abstract class to represent a synthetic data generator



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RecursiveBinarySearchTreeSet(AbstractSet):
    def __init__(self):
        self.root = None

    def searchElement(self, value):
        return self._searchElement(self.root, value) == value

    def _searchElement(self, node, value):
        if node is None:
            return None
        elif value == node.value:
            return node.value
        elif value < node.value:
            return self._searchElement(node.left, value)
        else:
            return self._searchElement(node.right, value)

    def insertElement(self, value):
        self.root, inserted = self._insertElement(self.root, value)
        return inserted

    def _insertElement(self, node, value, inserted=False):
        if node is None:
            inserted = True
            return Node(value), inserted
        elif value < node.value:
            node.left, inserted = self._insertElement(node.left, value, inserted)
        elif value > node.value:
            node.right, inserted = self._insertElement(node.right, value, inserted)
        elif value == node.value:
            node.value = value
        return node, inserted

myBST = RecursiveBinarySearchTreeSet()
values_to_add = [str(i) for i in range(60000)]
for value in values_to_add:
    myBST.insertElement(value)
print(myBST.searchElement(str(59000)))
print(myBST.insertElement(str(59000)))
print(myBST.insertElement(str(61000)))


