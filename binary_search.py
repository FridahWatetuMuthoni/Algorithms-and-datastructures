import math


def binary_search(list, target):
    """
    Description:
        The function searches a value in a list that is provided as an arguement
    Parameters:
        -list (type list): the list in which we are searching target from
        -target: the value that we are searching for in the list
    Returns: 
    The function returns the position at which the target was found else we return None
    """
    first = 0  # O(1)
    last = len(list) - 1  # O(1)

    while(first <= last):  # O(log n)
        middle = math.floor((first + last) / 2)

        if(list[middle] == target):  # O(1)
            return middle
        elif(list[middle] < target):  # O(1)
            first = middle + 1
        else:
            last = middle - 1

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target was not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 78, 46, 20, 15, 13]
numbers.sort()
print(numbers)
result = binary_search(numbers, 20)
verify(result)
