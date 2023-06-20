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


def sum(numbers, total=0):
    if (len(numbers) == 0):
        return total
    total += numbers[0]
    return sum(numbers[1:], total)


def sum_2(numbers):
    if (len(numbers) == 0):
        return 0
    print("Callng sum(%s)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    print("Call to sum(%s) returnung %d + %d" %
          (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum


def sum_loops(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum(numbers))
total = sum_2(numbers)
print(total)
