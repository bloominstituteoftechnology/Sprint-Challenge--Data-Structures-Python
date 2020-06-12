from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head




    def get(self):
        contents= []
        current = self.storage.head
        while current:
            contents.append(current.value)
            current = current.next
        return contents