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

    def reverse_list(self, node, prev=None):
        while node is not None:
            # we hold a reference for the node's next node
            next = node.next_node
            # in the beginning, set to None, like how the tail is set to None
            # Then afterwards the next_node is set to the prev node of the current nod
            node.next_node = prev
            # prev set to node for later use in the while loop
            prev = node
            # We then go on to the node's next node to change its pointer
            node = next
        # we set a new head of the final node that we changed
        self.head = prev
