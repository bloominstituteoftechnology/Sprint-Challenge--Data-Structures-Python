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
        prev_item = None
        current_item = self.head
        next_item = None
        while current_item:
            # Get to the next node
            next_item = current_item.next_node
            # Swap the next node to the prev node
            current_item.next_node = prev_item
            # Move onto the next node and repeat the process
            prev_item = current_item
            current_item = next_item
        self.head = prev_item
        
        