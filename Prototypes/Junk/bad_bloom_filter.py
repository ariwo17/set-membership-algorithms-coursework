class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * self.size

    def add(self, string):
        for seed in range(self.hash_count):
            hash_value = self.hash_function(string, seed)
            self.bit_array[hash_value] = 1

    def lookup(self, string):
        for seed in range(self.hash_count):
            hash_value = self.hash_function(string, seed)
            if self.bit_array[hash_value] == 0:
                return "Nope"
        return "Probably"

    def hash_function(self, string, seed):
        hash_value = 0
        for i in range(len(string)):
            hash_value = hash_value * seed + ord(string[i])
        return hash_value % self.size
