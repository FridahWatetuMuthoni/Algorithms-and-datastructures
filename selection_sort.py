import random
import sys

# You call this function with the path to a file you want to load.
# It loads the file contents, converts each line from a string to
# an integer, and returns them all as a Python list.
# The selection sort is O(n^2)


def load_numbers(file_name):
    numbers = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


numbers = load_numbers("numbers.txt")
print(numbers)


def selection_sort(values):
    sorted_list = []
    print("%-25s %-25s" % (values, sorted_list))
    for index in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sorted_list))
    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


sorted = selection_sort(numbers)
print(sorted)
