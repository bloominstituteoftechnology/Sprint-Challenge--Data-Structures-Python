from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        elif self.storage.length == self.capacity:
            if not self.storage.tail.next:
                self.storage.tail.next = self.storage.head
                self.current = self.storage.head
            self.current.value = item
            self.current = self.current.next

    def get(self):
        list_buffer_contents = []
        list_buffer_contents.append(self.storage.head.value)
        next_node = self.storage.head.next
        for i in range(self.capacity - 1):
            if next_node is None:
                pass
            else:
                list_buffer_contents.append(next_node.value)
                next_node = next_node.next

        return list_buffer_contents
