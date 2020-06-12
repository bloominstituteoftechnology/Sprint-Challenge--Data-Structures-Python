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
        if node:
            # tuple swap
            # prev becomes then next_node
            # then next_node becomes prev
            # 1st time through: node (1) pointing to 2    and prev to None.                 Code changes Prev to 2    and node (1) pointing to None.
            # 2nd time through: node (2) pointing to 3    and prev to 1 (pointing to None). Code changes Prev to 3    and node (2) pointing to 1. 
            # 3rd time through: node (3) pointing to None and prev to 2 (pointing to 1   ). Code changes Prev to None and node (3) pointing to 2. 
            prev, node.next_node = node.next_node, prev

        if prev: # If prev is not None then we have another element to swap
            self.reverse_list(prev, node)
        else: # We'll know we've gotten to the end when prev is None so set head to this node
            self.head = node
