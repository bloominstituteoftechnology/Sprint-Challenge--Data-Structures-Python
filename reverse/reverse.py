"""
Task 3. Reverse a Linked List
"""

class Node:
    """
    Node class for singly-linked list.
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        """
        Return the value stored in the node.
        """
        return self.value

    def get_next(self):
        """
        Return the subsequent node in the list, if any.
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Assign the subsequent node, as when inserting.
        """
        self.next_node = new_next

class LinkedList:
    """
    Singly-linked list class.
    """
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        """
        Insert a node at the head of the list.
        """
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        """
        Search the list for a value; return True if it is found, False
        otherwise.
        """
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """
        Without making it a doubly-linked list (adding a tail attribute),
        reverses the contents of the list using recursion, not a loop.
        """
        if node is None:
            # Empty list.
            return

        if node.get_next() is None:
            # At original tail.
            self.head = node
            return

        # Recursively reverse remainder of list.
        self.reverse_list(node.get_next(), node)

        # Node that was second from head will become second from tail.
        # Previous head becomes new tail.
        node.get_next().set_next(node)
        node.set_next(None)

    def reverse_list_loop(self, node, prev):
        """
        Without making it a doubly-linked list (adding a tail attribute),
        reverses the contents of the list using a loop, not recursion.
        """
        while node is not None:
            next_node = node.get_next()
            node.set_next(prev)
            prev = node
            node = next_node
        self.head = prev
