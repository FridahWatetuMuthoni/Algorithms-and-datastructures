# This function has a linear runtime
def linear_search(list, target):
    """
    Description:
        The function searches a value in a list that is provided as an arguement
    Parameters:
        -list (type list): the list in which we are searching target from
        -target: the value that we are searching for in the list
    Returns: 
    The function returns the position at which the target was found else we return None
    """
    for item in range(0, len(list)):  # O(n)
        if list[item] == target:  # O(1)
            return item
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target was not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = linear_search(numbers, 1)
verify(result)
