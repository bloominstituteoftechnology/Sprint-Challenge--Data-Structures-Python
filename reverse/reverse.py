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
        if not self.head or not self.head.next_node:
            return None

        if self.head.next_node:
            if node.next_node:
                current_next = node.next_node
            else:
                current_next = None
            if node is not self.head:
                # prev.next_node = node.next_node
                node.next_node = self.head
                self.head = node
            if current_next:
                self.reverse_list(current_next, None)


