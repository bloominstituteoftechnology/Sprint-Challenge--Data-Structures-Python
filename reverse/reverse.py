'''Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List.
 _Without_ making it a Doubly Linked List (adding a tail attribute), 
 complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list using recursion, *not a loop.*'''

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return
        
        # Check to see if the node does not point to another node
        if node.next_node is None:
            # Set the head to the current node
            self.head = node            
            # Set the next node to prev
            node.next_node = prev
            
        # Save node.next to set up for the recursive call
        next = node.next_node
        node.next = prev
        
        self.reverse_list(next, node)
            
