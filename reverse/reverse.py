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
        # base cases
        if node == None: # list is empty
            return
        if node.next_node == None: # we are now at end of list
            self.head = node # so set current node to head
            node.next_node = prev # and set next node to prev
            return
        else:
            nextnode = node.next_node
            node.next_node = prev
            self.reverse_list(nextnode, node) # reverse until we reach one of our base cases

