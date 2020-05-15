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
        # the value of the current node is our first param
        # the value of the previous node is our second param
        # we need to do this recurisevly
        if node is None:
            return None
        # ** if we are at the tail of our list --> set the tail to equal our new head
        # ** set the next node of the new head to equal the previous value
        if node.next_node is None:
            self.head = node
            node.next_node = prev
        else:
            # ** if we are not at the tail --> the node we pass into reverse list
            next_node = node.next_node
            node.next_node = prev
            self.reverse_list(next_node, node)


""" Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list using recursion, *not a loop.*

For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```

While credit will be given for a functional solution, only optimal solutions will earn a ***3*** on this task."""
