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
        inserted = False
        if element not in self.set:
            self.set.append(element)
            inserted = True
        return inserted

    def searchElement(self, element):
        found = False
        for member in self.set:
            if member == element:
                found = True
                break
        return found


import timeit

f = open("test1-mobydick.txt", "r")
book_words = []
current_word = ""
text = f.read()
for i in range(len(text)):
    if text[i] == ' ':
        book_words.append(current_word)
        current_word = ""
    else:
        current_word += text[i]
f.close()

f = open("test-search.txt", "r")
search_words = []
for x in f:
    search_words.append(x[0:len(x)-1])
f.close()

search = SequentialSearchSet()
insert_times = []
for n in book_words:
    start = timeit.default_timer()
    search.insertElement(n)
    end = timeit.default_timer()
    insert_times.append(end - start)
search_times = []
for m in search_words:
    start = timeit.default_timer()
    search.searchElement(m)
    end = timeit.default_timer()
    search_times.append(end - start)
