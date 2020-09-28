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
        if node and node.get_next():
            current = node
            while current:
                self.add_to_head(current.get_value())
                current = current.get_next()

#     def reverse_list(self):
#         prev = None
#         cur = self.head
#         nxt = self.head

#         while cur != None:
#             nxt = nxt.next_node
#             cur.next = prev
#             prev = cur
#             cur = nxt
#             print('Reverse list:', prev.value)
#         return prev

# rev = LinkedList()

# rev.add_to_head(1)
# rev.add_to_head(2)
# rev.add_to_head(3)
# rev.add_to_head(4)

# rev.reverse_list()