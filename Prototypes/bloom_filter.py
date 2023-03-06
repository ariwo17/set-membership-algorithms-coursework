import random
from bitarray import bitarray

EXPECTED_NUM_INSERTIONS = 500000
BITARRAY_SIZE = EXPECTED_NUM_INSERTIONS * 50
LN2 = 0.69314718056


class BloomFilterSet:
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
    def _optimise_k(m, n):
        return 1 + int(LN2 * (m / n))

    def insertElement(self, element):
        hash_values = self._hash(element)
        for value in hash_values:
            self.bit_array[value] = 1

    def searchElement(self, element):
        hash_values = self._hash(element)
        for value in hash_values:
            if not self.bit_array[value]:
                return False
        return True


myBF = BloomFilterSet(BITARRAY_SIZE)
myBF.num_hashes = myBF._optimise_k(myBF.size, EXPECTED_NUM_INSERTIONS)
to_add = [str(i) for i in range(EXPECTED_NUM_INSERTIONS)]
for member in to_add:
    myBF.insertElement(member)

false_positives = []
for i in range(EXPECTED_NUM_INSERTIONS, BITARRAY_SIZE):
    if myBF.searchElement(i):
        false_positives.append(i)

print(len(false_positives))
