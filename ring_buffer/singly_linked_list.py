class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value


class LinkedList:
    # Holds on to the first node and the last node
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, new_node):
        node = Node(new_node)

        if self.head is None and self.tail is None:
            self.tail = node
            self.head = node
        else:
            previous = self.tail
            previous.set_next_node(node)
            self.tail = node

    def remove_from_tail(self):
        if self.head and self.tail is None:
            return None

        elif self.head == self.tail:
            deleted = self.head.get_value()
            self.head = None
            self.tail = None
            return deleted

        else:
            deleted = self.tail.get_value()
            # The only way to get the second to last value is to go through the whole list from the beginning
            current = self.head
            # Keep iterating until the next_node == the deleted node
            while current.get_next_node() != self.tail:
                current = current.get_next_node()

            self.tail = current
            self.tail.set_next_node(None)
            return deleted

    def remove_head(self):
        deleted = self.head.get_value()
        if self.head and self.tail is None:
            return None

        elif self.head == self.tail:
            deleted = self.head.get_value()
            self.head = None
            self.tail = None
            return deleted

        else:
            self.head = self.head.get_next_node()
            return deleted

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next_node()

        return count

    def contains(self, value):
        current = self.head
        while current.next_node != None:
            if(current.get_value() == value):
                return True
            else:
                current = current.next_node()

        return False