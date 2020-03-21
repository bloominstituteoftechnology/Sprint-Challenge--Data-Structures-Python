from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
    
    def append(self, item):
        self.current = 0
        if self.current < self.capacity:
            self.storage.add_to_head(item)
            self.capacity += 1
        elif self.current == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
           
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        return list_buffer_contents
    
        # TODO: Your code here


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
