'''
Inside of the reverse directory, you'll find a basic implementation of a Singly Linked 
List. Without making it a Doubly Linked List (adding a tail attribute), complete the 
reverse_list() function within reverse/reverse.py reverse the contents of the list 
using recursion, not a loop.
'''

# Use Node class and LinkedList class as is
# Add reverse method to ll class that reverses the order on the single linked list

# Swap the head and the tail 
    # - This linked list doesn't have a tail parameter
    # - Just set the head to the last node in the original list
    # - When it reaches the end, there will be no next_node, set that to be the new head
# Set the previous node equal to the next node
    # The method tells us the previous node as input
    # The class has a next_node attribute


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
        # If there is no node passed in (the first test case)
        if node is None:
            return

        else:
            # Base case; If there is no next_node, it is the end of the linked list (the tail)
            # Set it to be the new head
            if node.next_node is None:
                self.head = node
                # Set the previous node (info we are recieve from the input) to be the node's next_node parameter
                node.next_node = prev
                return

            # If it is not the end of the list
            else:

                # Save the next_node to pass it to the method to traverse the list
                next_n = node.next_node

                # Set the current node's next_node attribute to the prev node given by the method's input
                node.next_node = prev

                # Re-call the method
                    # Pass in the next_node attribute as the node for the next cycle to work with
                    # Pass the node we just worked with as the previous node for the next cycle

                self.reverse_list(next_n, node)
