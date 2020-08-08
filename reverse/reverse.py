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
        if node is None: # CONDITION 1: NODE IS EMPTY 
            return

        if node.get_next() is None: # CONDITION 2: LINKED LIST HAS 1 OR MORE NODES | USE RECURSION TO GET TO THE END OF THE `SLL`
            self.head = node #  SET THE TAIL OF THE `SLL` AS THE HEAD OF `REVERSE_LIST`
            return

        self.reverse_list(node.get_next(), node) # REVERSE THE REST OF THE LIST, BY CONVERTING THE CURRENT NODE TO THE PREVIOUS NODE
        node.get_next().set_next(node) # SET THE VALUE OF WHAT WAS ORIGINALLY THE SECOND NODE, TO BE SECOND TO LAST
        node.set_next(None) # SET THE `NEXT` VALUE TO `NONE` ON THE NEW TAIL 
            