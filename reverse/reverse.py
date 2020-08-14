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
        if node is None:
            self.head = prev
            return

        next = node.get_next()
        node.set_next(prev)
        self.reverse_list(next, node)

list = LinkedList()
list.add_to_head(1)
list.add_to_head(3)
list.add_to_head(5)
list.add_to_head(7)

print(f"Value for head is {list.head.value}")
list.reverse_list(list.head, None)
print(f"New value for head is {list.head.value}")
















