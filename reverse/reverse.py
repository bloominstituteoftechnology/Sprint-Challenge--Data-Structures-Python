"""
Task 3. Reverse a Linked List

Without making it a Doubly Linked List (adding a tail attribute), 
complete the reverse_list() function within reverse/reverse.py 
***reverse the contents of the list using recursion, not a loop.***

While credit will be given for a functional solution, 
only optimal solutions will earn a 3 on this task.
"""

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

    def reverse_list(self, node, prev): #actually can use loop but NO TAIL ATTRIBUTE
        if node is None: # is node is empty 
            return
        
        if node.get_next() is None: # set tail of sll as head of new reversed list
            self.head = node
            return

        self.reverse_list(node.get_next(), node) # recursively reversing by converting the current node to the previous one

        node.get_next().set_next(node) # set node that was second from the head to become second from tail
        node.set_next(None) # next value becomes none on new tail