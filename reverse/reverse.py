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
        # Iterative
        while node:
            # Make storage for the passed node's next node
            next = node.get_next()
            # Change the next node to the previous node
            node.next_node = prev
            # Move the previous and current node up
            prev = node
            node = next
            self.head = prev


        # Recursive - BUG

        # # Check if head is empty or has reached the end of the list
        # if self.head is None or self.head.next_node is None:
        #     return self.head
        # # Reverse the everything behind the current self.head
        # modified_list = self.reverse_list(self.head.next_node, self.head.prev)

        # # Move the first element to the end
        # self.head.next_node.next_node = self.head
        # self.head.next_node = None

        # # Move the head pointer
        # return modified_list

