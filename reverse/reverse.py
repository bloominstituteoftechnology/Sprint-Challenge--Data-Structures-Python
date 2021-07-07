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

    # has to use recursion to reverse the linked list
    def reverse_list(self, node, prev):

        # stop if given an empty linked list
        if node is None:
            return
        
        # check if we're at the tail
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        
        # this will become the "current" node next time
        next_node = node.next_node
        # previous node becomes new "next" node 
        node.next_node = prev

        # keep er goin (next_node will become current node, node will become previous)
        self.reverse_list(next_node, node)
        