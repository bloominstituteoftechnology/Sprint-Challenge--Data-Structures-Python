
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            if self.head.get_next_node() is None:
                head = self.head
                self.head = None
                self.tail = None
                return head.get_value()
            value = self.head.get_value()
            self.head = self.head.get_next_node()
            return value

    def remove_tail(self):
        if not self.head:
            return None
        value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.next_node.get_next_node() is not None:
            current = current.next_node
        self.tail = current
        return value

    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next_node()
        return False

    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        max_value = 0
        while cur_node is not None:
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()
        return max_value

