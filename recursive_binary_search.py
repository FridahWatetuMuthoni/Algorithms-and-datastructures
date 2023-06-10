import math


def recursive_binary_search(list, target):
    if(len(list) == 0):
        return False
    else:
        middle = math.floor(len(list) / 2)

        if(list[middle] == target):
            return True
        else:
            if list[middle] < target:
                return recursive_binary_search(list[middle + 1:], target)
            else:
                return recursive_binary_search(list[:middle - 1], target)


def verify(result):
    print(f"Target found: {result}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 78, 46, 20, 15, 13]
numbers.sort()
result = recursive_binary_search(numbers, 78)
verify(result)
