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
        # No tail attribute in provided prompt starter code.

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if self.head is None:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """
        Reverse the order of the items in the linked list, in place. 
        Return the new list (for ease of use).
        """        
        # Reverse the list in place:
        # Runtime: O(n)
        prev = None
        current = self.head
        while current is not None:      # This already addresses case of empty LL.
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        
        # Set the LL's original tail (prev, because current is now None) as its new head:
        self.head = prev

    def print_values(self):
        """
        Print the value of every node in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.value)
            current = current.get_next()
