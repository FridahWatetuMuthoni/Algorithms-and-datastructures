import random
import sys

# You call this function with the path to a file you want to load.
# It loads the file contents, converts each line from a string to
# an integer, and returns them all as a Python list.


def load_numbers(file_name):
    numbers = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


numbers = load_numbers("numbers.txt")
print(numbers)

# The Quicksort runtime for bestcase is O(n log n)
# The Quichsort runtime for worstcase is o(n^2)
# Hence the Quicksort runtime is O(n log n)


def quicksort(values):
    if (len(values) <= 1):
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %ls %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return (quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot))


sorted_numbers = quicksort(numbers)
print(sorted_numbers)
