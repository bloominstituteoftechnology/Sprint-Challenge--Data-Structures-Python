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

    def __str__(self):
        return f"Value: {self.value}, Next_Node: {self.next_node}"


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

        print("ADD TO HEAD")
        print(f"Head: {self.head}")

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

        # check if LL is empty
        if self.head is None:
            return

        # store current node
        cur_node = node
        # store next node
        next_node = cur_node.next_node
        # make next node the prev
        cur_node.set_next(prev)

        # loop through all nodes until None
        while next_node is not None:

            # store previous node
            prev_node = cur_node

            # store current node
            cur_node = next_node

            # store next node of current node
            next_node = cur_node.get_next()

            # reverse cur_node pointer to previous node
            cur_node.set_next(prev_node)

        # set head to new current node
        self.head = cur_node

        print("REVERSE LIST")
        print(f"Head: {self.head}")


linked_list = LinkedList()

linked_list.add_to_head(3)
linked_list.add_to_head(2)
linked_list.add_to_head(1)
linked_list.reverse_list(linked_list.head, None)
