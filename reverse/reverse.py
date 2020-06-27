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

        # Find the last node, set it to head, and reverse it's next pointer to be previous
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        
        # Next node to evaluate starts at the node.next & move it once each time to loop through the list
        next = node.next_node
        
        # Set node.next to be the prev value, essentially reversing it's arrow
        node.next_node = prev
        
        # Recursive solution
        self.reverse_list(next, node)
