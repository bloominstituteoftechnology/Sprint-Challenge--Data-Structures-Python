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

    def reverse_list(self, node, prev=None):
        # handles the test_empty_reverse test
        if node is None and prev is None:
            return
        else:
            # This conditional is triggered when the recursion
            # hits the end of the list
            if node.next_node is None:
                self.head = node
                node.next_node = prev
                return
            
            # Have to define _next before calling reverse_list because
            # we overwrite it in the next line
            _next = node.next_node
            node.next_node = prev

            self.reverse_list(_next, node)

    def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()

ll = LinkedList()
ll.add_to_head(3)
ll.add_to_head(5)
ll.add_to_head(9)
ll.add_to_head(11)
ll.print_ll_elements()
ll.reverse_list(ll.head, None)