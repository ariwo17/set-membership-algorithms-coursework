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


class AbstractTestDataGenerator(ABC):

    # constructor
    @abstractmethod
    def __init__(self):
        pass

        # creates and returns a list of length "size" of strings

    # size : int
    # data : list<str>
    @abstractmethod
    def generateData(self, size):
        data = [""] * size
        return data


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RB_Node(Node):
    RED = True
    BLACK = False

    def __init__(self, value, colour):
        super().__init__(value)
        self.colour = colour


class SequentialSearchSet(AbstractSet):

    def __init__(self):
        self.set = []

    def insertElement(self, element):
        if self.searchElement(element) is False:
            self.set.append(element)
            return True
        return False

    def searchElement(self, element):
        for member in self.set:
            if member == element:
                return True
        return False


# mySS = SequentialSearchSet()
# mySS.set = [str(i) for i in range(60000)]
# print(mySS.searchElement(str(59000)))


class BinarySearchTreeSet(AbstractSet):

    def __init__(self):
        self.root = None

    def insertElement(self, element):
        if not self.root:
            self.root = Node(element)
            return True
        else:
            current = self.root
            while current:
                if current.value == element:
                    return False
                elif current.value > element:
                    if not current.left:
                        current.left = Node(element)
                        return True
                    current = current.left
                elif current.value < element:
                    if not current.right:
                        current.right = Node(element)
                        return True
                    current = current.right
        return False

    def searchElement(self, element):
        current = self.root
        while current:
            if current.value == element:
                return True
            elif current.value > element:
                current = current.left
            elif current.value < element:
                current = current.right
        return False


myBST = BinarySearchTreeSet()
values_to_add = [str(i) for i in range(60000)]
for value in values_to_add:
    myBST.insertElement(value)
print(myBST.searchElement(str(59000)))
print(myBST.insertElement(str(59000)))
print(myBST.insertElement(str(61000)))


class BalancedSearchTreeSet(AbstractSet):
    def __init__(self):
        self.root = None

    @staticmethod
    def is_red(node):
        if node is None:
            return False
        return node.colour == RB_Node.RED

    @staticmethod
    def rotate_left(node):
        x = node.right
        node.right = x.left
        x.left = node
        x.colour = node.colour
        node.colour = RB_Node.RED
        return x

    @staticmethod
    def rotate_right(node):
        x = node.left
        node.left = x.right
        x.right = node
        x.colour = node.colour
        node.colour = RB_Node.RED
        return x

    @staticmethod
    def flip_colours(node):
        node.colour = RB_Node.RED
        node.left.colour = RB_Node.BLACK
        node.right.colour = RB_Node.BLACK

    def insertElement(self, element):
        self.root, inserted = self._insertElement(self.root, element)
        self.root.colour = RB_Node.BLACK
        return inserted

    def _insertElement(self, node, element):
        if node is None:
            return RB_Node(element, RB_Node.RED), True

        if element < node.value:
            node.left, inserted = self._insertElement(node.left, element)
        elif element > node.value:
            node.right, inserted = self._insertElement(node.right, element)
        else:
            return node, False

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colours(node)

        return node, inserted

    def searchElement(self, element):
        return self._searchElement(self.root, element) == element

    def _searchElement(self, node, element):
        if node is None:
            return False

        if element < node.value:
            return self._searchElement(node.left, element)
        elif element > node.value:
            return self._searchElement(node.right, element)
        else:
            return node.value


# myLLRB_BST = BalancedSearchTreeSet()
# values_to_add = [str(i) for i in range(60000)]
# for value in values_to_add:
#     myLLRB_BST.insertElement(value)
# print(myLLRB_BST.searchElement(str(59000)))
# print(myLLRB_BST.insertElement(str(59000)))
# print(myLLRB_BST.insertElement(str(61000)))
#






import random
from bitarray import bitarray

EXPECTED_NUM_INSERTIONS = 500000
BITARRAY_SIZE = EXPECTED_NUM_INSERTIONS * 50
LN2 = 0.69314718056


class BloomFilterSet(AbstractSet):
    def __init__(self, size, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hash(self, element):
        hash_values = []
        for i in range(self.num_hashes):
            hash_value = hash(f'{element}{i}')
            hash_values.append(hash_value % self.size)
        return hash_values

    @staticmethod
    def optimise_k(m, n):
        return 1 + int(LN2 * (m / n))

    def insertElement(self, element):
        if self.searchElement(element) is False:
            hash_values = self._hash(element)
            for value in hash_values:
                self.bit_array[value] = 1
            return True
        else:
            return False

    def searchElement(self, element):
        hash_values = self._hash(element)
        for value in hash_values:
            if not self.bit_array[value]:
                return False
        return True

#
# myBF = BloomFilterSet(BITARRAY_SIZE)
# myBF.num_hashes = myBF._optimise_k(myBF.size, EXPECTED_NUM_INSERTIONS)
# to_add = [str(i) for i in range(EXPECTED_NUM_INSERTIONS)]
# for member in to_add:
#     myBF.insertElement(member)

# false_positives = []
# for i in range(EXPECTED_NUM_INSERTIONS, BITARRAY_SIZE):
#     if myBF.searchElement(i):
#         false_positives.append(i)
#
# print(len(false_positives))


import random
import string

NUM_WORDS = 50000
MIN_LENGTH = 1
AV_LOW_LENGTH = 2
AV_HIGH_LENGTH = 6
MAX_LENGTH = 12
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'

output_file = "synthetic_data.txt"

SAMPLE_INTERVAL = 200
test_file = "../Archive(got from moodle)/testfiles/synthetic_test_search.txt"
test_words = set()


def generate_word(scarcity=0.05):
    limit = int(1 / scarcity)
    roulette = random.randint(0, int(1 / scarcity))
    if roulette == limit:
        length = random.randint(AV_LOW_LENGTH, AV_HIGH_LENGTH)
    else:
        length = random.randint(MIN_LENGTH, MAX_LENGTH)
    word = ''
    for i in range(length):
        if i % 2 == 1 or length == 1:
            word += random.choice(VOWELS)
        else:
            word += random.choice(CONSONANTS)
    return word

# # Generate the words and write them to the output file
# with open(output_file, 'w') as f:
#     for i in range(NUM_WORDS):
#         word = generate_word()
#         f.write(word)
#         if i % SAMPLE_INTERVAL == 0:
#             test_words.add(word)
#             test_words.add(generate_word())
#         if i <= NUM_WORDS:
#             f.write(' ')
#
# test_words = list(test_words)
# with open(test_file, 'w') as f:
#     for i in range(len(test_words)):
#         f.write(test_words[i])
#         if i <= len(test_words):
#             f.write('\n')
#
# print(repr(test_words))
# print(len(test_words))
