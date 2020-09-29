class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next = next_node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class dll:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0
        self.current_position = ListNode(None)

    def __len__(self):
        return self.length

    def delete(self, node):
        if self.head is None:
            return None

        elif self.head == self.tail:
            self.head = None
            self.tail = None

        elif node is self.head:
            self.head = self.head.next
            node.delete()

        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()

        else:
            node.delete()

        self.length -= 1

    def add_to_head(self, new_node):

        if self.head is None:
            self.head = new_node
            self. tail = new_node
            self.current_position = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.current_position = self.head
            self.delete(self.head.next)

            print("head", self.head.value)
            print("current", self.current_position.value)

        self.length += 1

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head is self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.current_position = self.head

        self.length += 1

    def add_to_full_tail(self, node):

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        self.delete(node.prev)

    def insert(self, current_node, replacement):
        new_node = ListNode(replacement)

        if current_node is self.head:
            self.add_to_head(new_node)
        elif current_node is self.tail:
            self.add_to_full_tail(new_node)
        else:
            # current_node.prev.next = new_node
            # new_node.next = current_node.next
            # new_node.prev = current_node.prev
            # current_node.next.prev = new_node
            nxt = current_node.next
            current_node.next = new_node
            new_node.next = nxt
            new_node.prev = current_node
            nxt.prev = new_node

        self.length += 1


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = dll()
        self.append_count = 0

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        else:

            if self.storage.current_position is self.storage.head:
                self.storage.insert(self.storage.current_position, item)
                self.storage.current_position = self.storage.current_position.next
                self.append_count += 1

            elif self.storage.current_position is self.storage.tail:
                self.storage.insert(self.storage.current_position, item)
                self.storage.current_position = self.storage.head
                self.append_count += 1

                self.append_count = 0

            else:

                self.storage.insert(self.storage.current_position, item)
                self.storage.delete(self.storage.current_position)
                self.append_count += 1

                if self.append_count <= self.capacity:

                    self.storage.current_position = self.storage.current_position.next.next

                # else:

                #     self.storage.current_position = self.storage.head
                #     self.append_count = 0

    def get(self):
        node_list = []
        current_node = self.storage.head

        while current_node is not None:
            node_list.append(current_node.value)

            current_node = current_node.next

        return node_list
