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
            return

        # print("self.head.next_node,", node.next_node.value)

        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
        else:
            self.reverse_list(node.next_node, node)
            node.next_node = prev

        # if self.head is None:
        #     return
        # if node is self.head and node.next_node is None:
        #     return
        # if node is self.head:
        #     self.reverse_list(node.next_node, node)

        print("node", node)
        print("prev", prev)


ll = LinkedList()
ll.add_to_head(2)
ll.add_to_head(4)
ll.add_to_head(7)
# print("ll value", ll.head.get_next.)
print("prev", ll.head)
print(ll.contains(0))
print()
# ll.reverse_list(self.head, 2)
# print(ll.reverse_list(2, 4))
