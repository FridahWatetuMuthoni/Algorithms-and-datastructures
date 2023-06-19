from linked_list import Linked_List


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    -Recursively divide the linked list into sublists containing a single node
    -Repeatedly merge the sublist to produce sorted sublists until one remains
    Return a sorted linked list
    O(n) * O(k log n) = O(kn log n)
    Runs in O(kn log n)
    """
    if (linked_list.size() == 1):
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """ 
    Divide the unsorted list at midpoint into sublists
    Takes O(k log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid-1)  # O(k log n)
        left_half = linked_list
        right_half = Linked_List()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """ 
    This function merges two linked list, sorting data in nodes
    Returns a new, merged list
    Runs in O(n) time
    """
    # Create a new linked list that contains nodes from merging left and right
    merged_list = Linked_List()

    # Add a fake head that is discarded later
    merged_list.add(0)

    # set current to the head of the linked list
    current = merged_list.head

    # Obtain head nodes for left and right
    left_head = left.head
    right_head = right.head

    # iterating over left and right untill we reach the tail node of either
    while (left_head or right_head):
        # if the head node of left is None, were past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to step the loop condition to False
            right_head = right_head.next_node

        # if the head node of right is None, were past the tail
        # Add the node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            # Not at either tail node
            # Obtain ode data to perform comparison operations
            # compare values at each index position
            left_data = left_head.data
            right_data = right_head.data
            if (left_data < right_data):
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # move current to next node
        current = current.next_node

    # discard the fake head and set the first merged node as head
    head = merged_list.head.next_node
    merged_list.head = head

    return merged_list


l = Linked_List()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
