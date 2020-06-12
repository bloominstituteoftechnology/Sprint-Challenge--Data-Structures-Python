class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
#good
    def get_value(self):
        return self.value
#good

    def get_next(self):
        return self.next_node
#good

    def set_next(self, new_next):
        self.next_node = new_next
#good

class LinkedList:
    def __init__(self):
        self.head = None
#good

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
#good

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
#good

    def reverse_list(self, node, prev):
        if node == None or node.next_node == None:
            self.head = node
        else:
            self.reverse_list(node.next_node, node)#calls again throwing in last node as first and first as last to filps list
            node.next_node.next_node = node
            node.next_node = None
