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
        
        curr_node = node

        # While loop will run until the next_node is None (AKA the tail)
        while curr_node:
            # Set next_node to a variable for the next time around
            next_node = curr_node.next_node
            # This line does the reversing. Essentially bring the current node
            #. to the head of this list. 
            curr_node.next_node = prev
            # Set prev to a variable to it can be used the next time through
            #. Will be the first node the first time through, second node the 
            #. second time through, and so on.
            prev = curr_node
            # Update the curr_node so loop runs again or exits if None
            curr_node = next_node
    
        # Update the head of the list to be the last prev variable before the
        #. loop exited
        self.head = prev 
        

        
