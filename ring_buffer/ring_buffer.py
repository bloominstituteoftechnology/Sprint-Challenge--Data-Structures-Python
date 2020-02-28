from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.count = 0

    def append(self, item):
        self.storage.add_to_tail(item)
        if self.storage.__len__() > self.capacity:
            self.storage.remove_from_head()

        self.count += 1
        if self.count == self.capacity:
            self.count = 0
            self.current = self.storage.tail
        
    def get(self):
        # Note: This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.current:
            node = self.current.next
            while node:
                list_buffer_contents.append(node.value)
                node = node.next

        node = self.storage.head 
        while node != self.current:
            list_buffer_contents.append(node.value)
            node = node.next
        
        if self.current:
            list_buffer_contents.append(self.current.value)

        return list_buffer_contents


# ----------------Stretch Goal-------------------

# Using list rather than array here

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = None # This is a list index.
        
    def append(self, item):
        if self.current is None:
            self.current = 0 
        else:
            self.current += 1

        if self.current == len(self.storage):
            self.current = 0

        self.storage[self.current] = item
        
    def get(self):
        return [i for i in self.storage if i]