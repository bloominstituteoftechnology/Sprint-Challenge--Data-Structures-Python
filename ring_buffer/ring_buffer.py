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
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        

        # TODO: Your code here
        for i in range(len(self.storage)):
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.full = False
        self.storage = [0] * capacity

    def append(self, item):
        self.storage[self.current] = item
        
        if self.current == (self.capacity - 1):
            self.full = True
            self.current = 0
        else:
            self.current += 1


    def get(self):
        if self.full:
            return self.storage
        else:
            return self.storage[:self.current]