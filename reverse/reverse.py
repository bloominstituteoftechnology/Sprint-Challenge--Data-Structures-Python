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

# Create and handle list operations
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

    # Method to reverse linked list
    def reverse_list(self, node, prev):
        # Divide list into first node and rest of linked list
        while node:
        # Call reverse for the rest of the linked list
            next_node = node.get_next()
            prev = node 
        # Link rest to first
            node = next_node
        #fix head pointer
        self.head = prev
