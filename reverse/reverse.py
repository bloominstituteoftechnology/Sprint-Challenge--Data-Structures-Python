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
        if self.head: #list has data

            if node.next_node: # has next node
                next_value = node.next_node # grab next node data before flip
                node.next_node = prev # flip direction of the list 
                self.reverse_list(next_value, node) # pass next node to itself
            else: # no next node
                self.head = node # point to self
                node.next_node = prev # connect to list
                return False
        else:
            return False



