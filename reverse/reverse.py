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
        self.tail = None

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
        # if node is None:
        #     return None
        # elif node.next_node is None:
        #     return self.head
        # else:
        #     prev = None
        #     while node.get_next() is not None:
        #         node.next_node = prev
        #         prev = node
        #         node = node.get_next()


        while node is not None:
            # print('node A:', node.value)
            next_ = node.next_node
            node.next_node = prev
            prev = node
            node = next_
            # print('node B:', node.value)
        
        self.head = prev

    def __str__(self):
        node = self.head
        output = ''
        while node.get_next() is not None:
            output + f'{node.value}'
            node = node.get_next()
        return output
