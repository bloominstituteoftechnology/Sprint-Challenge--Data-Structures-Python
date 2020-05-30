from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None 
        self.storage = DoublyLinkedList()

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
            self.current = self.storage.head
        
        else:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
                self.current = self.storage.tail

            else:
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
        
    def get(self):
        list_buffer_contents = []
        for i in range(len(self.storage)):
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next
        return list_buffer_contents