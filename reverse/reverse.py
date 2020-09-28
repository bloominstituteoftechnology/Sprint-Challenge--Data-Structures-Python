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
        # if not the head, return False
        if not self.head:
            return False
        # set current = to head
        current = self.head
        while current:
            # if the value of head = value
            if current.get_value() == value:
                return True
            # move on to the next
            current = current.get_next()
        return False

    def reverse_list(self, node, prev):
        # while current node exists 
        if node:
            # store the next node
            next_node = node.next_node
            # set the prev node to the next node
            node.next_node = prev
            # run it all through again, with the new root
            self.reverse_list(next_node, node)
        # if node is None
        else:
            # the previous node is the head
            self.head = prev

# this didn't push through Git the first time, comment to try again