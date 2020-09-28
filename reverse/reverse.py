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
        current_node = self.head

        # create list to hold nodes as they get removed
        stack = []

        # removing nodes and adding to list
        while current_node != None:
            stack.append(current_node.get_value())
            current_node = current_node.get_next()

        # Using LIFO from stack
        if len(stack) > 0:
            self.head = Node(stack.pop())
            current_node = self.head

            while len(stack) > 0:
                current_node.set_next(Node(stack.pop()))
                current_node = current_node.get_next()

"""
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
"""

if __name__ == "__main__":
    ll = LinkedList()

    ll.add_to_head(1)
    ll.add_to_head(2)
    ll.add_to_head(10)

    print(ll.reverse_list(ll.head, None))
    #unsure how to test
    # tests run but reverse_list returns None