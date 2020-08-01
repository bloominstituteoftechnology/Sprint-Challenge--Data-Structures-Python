from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            # remove item from head
            remove_item = self.storage.head
            self.storage.remove_from_head()
            #append new item to tail
            self.storage.add_to_tail(item)
            if remove_item == self.current:
                self.current = self.storage.tail

    def get(self):
        pass