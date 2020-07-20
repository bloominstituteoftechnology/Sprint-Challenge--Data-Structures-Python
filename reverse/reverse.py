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
        # check for empty head
        # and return if head is None
        if not self.head:
            return
        # check to make sure there is a next node
        # if not, set the head to the node
        # set the node's next node to prev
        # and return
        if not node.next_node:
            self.head = node
            node.next_node = prev
            return

        # else create a new pointer to the next node
        next = node.next_node
        # set the node's next node to the prev value
        node.next_node = prev
        # and recursively call reverse_list again
        self.reverse_list(next, node)



        

# Test cases before running Unit tests
# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# print(list.head.value) # should be 5
# print(list.head.get_next().value) # should be 4
# print(list.head.get_next().get_next().value) # should be 3
# print(list.head.get_next().get_next().get_next().value) # should be 2
# print(list.head.get_next().get_next().get_next().get_next().value) # should be 1
# list.reverse_list(list.head, None)
# print(list.head.value) # should be 1
# print(list.head.get_next().value) # should be 2
# print(list.head.get_next().get_next().value) # should be 3
# print(list.head.get_next().get_next().get_next().value) # should be 4
# print(list.head.get_next().get_next().get_next().get_next().value) # should be 5