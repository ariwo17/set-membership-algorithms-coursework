import timeit


# Linear search
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False


words = []
with open("test1-mobydick.txt", "r") as file:
    for line in file:
        words.append(line)


if __name__ == "__main__":
    print("TRIAL ONE: ", timeit.timeit(lambda: linear_search(words, "degree"), number=5000))
    print("TRIAL TWO: ", timeit.timeit(lambda: linear_search(words, "degree"), number=5000))
    print("TRIAL THREE: ", timeit.timeit(lambda: linear_search(words, "degree"), number=5000))
