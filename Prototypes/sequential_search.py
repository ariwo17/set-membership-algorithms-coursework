import timeit


# Linear search
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False
