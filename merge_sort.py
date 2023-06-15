def merge_sort(list):
    """ 
    The function sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    merge= O(n)  slipt= O(log n)
    O(n) * O(log n) = O(n log n)
    takes overall O(n log n) time
    """
    # Base case: If the list has only one element, it is already sorted
    if (len(list) <= 1):
        return list

    # Divide the list into two halves
    left_half, right_half = split(list)

    # Recursively sort the two halves
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge the sorted halves and return them
    return merge(left, right)


def split(list):
    """ 
    Divides the unsorted list at midpoint into sublist
    Returns two sublists- left and right
    takes overall O(log n) time
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """ 
    The function merges two list(arrays), and sorts them in the process
    Returns a new merged list
    takes overall O(n) time
    """
    new_list = []
    i = 0  # for indexes in the left list
    j = 0  # for indexes in the right list

    # Compare elements from the left and right sublists
    # and add the smaller one to the merged list
    while (i < len(left) and j < len(right)):

        if (left[i] < right[j]):
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    # Add the remaining elements from the left sublist, if any
    while (i < len(left)):
        new_list.append(left[i])
        i += 1

    # Add the remaining elements from the right sublist, if any
    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


def verify_sorted(list):
    n = len(list)

    if (n == 0 or n == 1):
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(l)
print(verify_sorted(l))
