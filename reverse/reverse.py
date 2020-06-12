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
        # if the node is None -> do nothing 
        if not node:
            return
        # the node is the last one when the next_node is None
        if not node.next_node:
            # set the last node as the head of reversed list
            self.head = node
            # the second node in the reverse list
            # should be the pre-last node in the original list
            # change the pointer of the next_node to be the previous node
            node.next_node = prev
            return

        # Now go to the next node, which is actually the previous node
        # because node.next_node = prev
        # prev should be the next item in the original list,
        # which is actually the node that was previously added in the reversed list
        # reapply the method
        self.reverse_list(node.next_node, prev=node)
        # change the pointer for the next_node to be the previous node from original list
        node.next_node = prev
        return
