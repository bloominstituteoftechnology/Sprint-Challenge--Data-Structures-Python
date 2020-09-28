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
        if not self.head:
            return

        # I couldn't quite figure out this method:      
        # new_head = self.head # temporary
        # current = self.head
        # next = current.next_node
        # end = None
        # if next:
        #     end.next_node = None
        #     while next:
        #         current = next
        #         next = current.next_node
        #         if next is None:
        #             new_head = current
        # self.head = new_head

        # list = []
        # current = self.head
        # while current.next_node:
        #     list.append(current.value)
        #     current = current.next_node
        # while len(list) > 0:
        #     # still not there, but close. I bet if I sleep on it I'll get it.
        #     # need to tweak this:
        #     current.next_node = Node(list.pop())

        # okay, need a previous variable. works now!
        prev = None
        current = self.head
        while current:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
