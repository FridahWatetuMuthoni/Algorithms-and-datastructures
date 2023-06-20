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

# merge sort runtime O(n log n)


def merge_sort(values):
    if (len(values) <= 1):
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    print("%15s %-15s" % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values


sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
