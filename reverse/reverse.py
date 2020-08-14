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
        # youve got this dont give up yet.
        # You know how to do this.

        # Check if the node is None:
        if node is None:
            return
        # YESSS THIS WORRKKKSKKSKSKKS ahh yeah.
        # check if the list only has one element then we set the head pointer to this node
        elif node.next_node is None:
            self.head = node
            self.head.next_node = prev
            return self.head
            # if it has more pass the next node of node to the reverse method
        else:
            reversed = self.reverse_list(node.next_node, prev)
            node.next_node.next_node = node
            node.next_node = prev
            return reversed
