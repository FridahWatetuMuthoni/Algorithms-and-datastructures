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


def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


sorted = bogo_sort(numbers)
print(sorted)
