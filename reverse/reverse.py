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
        #if no items in the list
        if not self.head:
            return node
        
        #if at the end of the list
        if not node.next_node:
            self.head = node #declare new head node ('tail' of the list)
            node.next_node = prev #set current node's next_node to point to the prev node that was passed in the function
            return

        #if not yet at the end of the list, keep changing the current node's next_node and continue to traverse the list
        nextNode = node.next_node #set next node
        node.next_node = prev #set current node's next_node to point to the prev node that was passed in the function
        self.reverse_list(nextNode, node)