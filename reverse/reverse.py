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
        if self.head is None: # if self.head is none
            return # then do nothing
        if node.next_node is None: # if the next node is none (meaning it's the tail)
            self.head = node # set the head as this node (start the list)
            node.next_node = prev # this node's next node is really the one before it
            return # get outta here
        next_thing = node.next_node # declare variable
        node.next_node = prev # node's NEXT is prev
        self.reverse_list(next_thing, node) # recursion: next_thing will become node parameter, and node will become the prev parameter
        