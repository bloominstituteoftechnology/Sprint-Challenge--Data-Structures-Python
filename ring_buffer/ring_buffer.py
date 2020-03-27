from doubly_linked_list import DoublyLinkedList

# You want to define a buffer with a fixed size, 
# so that when it fills up, adding another element must overwrite the first (oldest) one. 
# This kind of data structure is particularly 
# useful for storing log and history information. 

# A ring buffer is a non-growable buffer with a fixed size. 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        

# When the ring buffer is full and a new element is inserted, 
# the oldest element in the ring buffer is overwritten with the newest element.
    def append(self, item):
        """append an element at the end of the buffer"""
        self.storage.add_to_tail(item)
        if self.storage.length ==self.capacity:
            self.current = 0

            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
