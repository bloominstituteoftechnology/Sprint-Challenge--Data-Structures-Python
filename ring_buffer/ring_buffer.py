from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.capacity > len(self.storage):
            self.storage.add_to_tail(item)
            if len(self.storage) == 1:
                self.oldest = self.storage.head
        
        else:
            self.oldest.value = item

            if self.oldest is not self.storage.tail:
                self.oldest = self.oldest.next
            else:
                self.oldest = self.storage.head

        

    def get(self):
        ring_buffer_list = []
        node = self.storage.head
        while node is not None:
            ring_buffer_list.append(node.value)
            node = node.next

        return ring_buffer_list