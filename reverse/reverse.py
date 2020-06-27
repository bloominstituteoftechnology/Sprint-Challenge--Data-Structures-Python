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
    
    # If an empty list, return None because there is nothing to reverse
    def reverse_list(self, node, prev):
        
        if self.head is None:
            return

        # If it's the last node, set it to head, and reverse it's next pointer to be previous
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        
        # Else, we have pointers: 
        # next to evaluate the start node's next value to be able to hit each element in the list
        # node.next_node set to the prev value of the current node, reversing it's arrow (initialized as None if called on head node)
        next = node.next_node
        node.next_node = prev

        # Recursive solution to move through the nodes in the list
        self.reverse_list(next, node)