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
        #Steps: We are trying to swap the positions to change their value
        #1. if the node exists then we are going to swap the values ç
        # so the prev node will become the next node and the node that prev was becomes to none.
        # example: 1->2->3->None, 3->2->1->None
        if node:

            prev, node.next_node = node.next_node, prev
        # if prev node exists then we have the prev node to move more forward by incrementing the number of node.
        # and the former node goes back in a lesser number of node.
        if prev: #
            #using the recursive method to swap.
            self.reverse_list(prev, node)
        else: # 3->2->1->None
            # this wil identify that we have reached to the end point and it wil default the node to head.
            self.head = node
