# Singley Linked List
""" 
You can add a node to the linked list in three different ways:
1. At the head of the list-> prepend: this means that the first node is at the tail and the last node it the head
2. At the end of the list->append: this means that the head is the first node created and the tail is the last node 
created
3. Inserting a node at a specific position
"""


class Node:
    """ 
    An object for storing a single node of a linked list
    Models two attributes 
    data => the value contained in the linked list
    next_node=> the pointer/link to the next node in the linked list
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node data: {self.data}"


class Linked_List:
    """ 
    The linked list class is used to create  a linked list using the nodes created
    It defends the head of the linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        if (self.head == None):
            return True
        else:
            return False

    def size(self):
        """ 
        Returns the number of nodes in the list
        The function has a time complexy of linear time O(n)
        """
        current = self.head
        count = 0

        while (current != None):
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """ 
        Adds a new node at the head of the linked list
        this operation takes consant time-> O(1)
        """
        new_node = Node(data)
        # if there was no other node it sets the next_node of the new node to None
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or None if not found
        Takes 0(N) 
        """
        current = self.head

        while (current != None):
            if (current.data == key):
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """ 
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        Take overall O(n)
        """

        if (index == 0):
            self.add(data)
        if (index > 0):
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """ 
        Removes Node containing data that matches the key 
        Returns the node or None if the key doesnt exists
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while (current and not found):
            if (current.data == key and current.data == self.head):
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while (position < index):
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """ 
        Returns a string representation of the list and it takes O(n) time
        """
        nodes = []
        current = self.head

        while (current != None):
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append((f"[Tail: {current.data}]"))
            else:
                nodes.append(f"{current.data}")

            current = current.next_node
        return "->".join(nodes)


"""
linked = Linked_List()
linked.add(20)
linked.add(30)
linked.add(40)
linked.add(50)
print(linked.size())
print(linked)
print(linked.search(400))
"""
