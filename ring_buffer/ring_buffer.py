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
        pass