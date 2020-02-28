from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity <= self.storage.length: 
            self.storage.remove_from_head()
        else: 
            self.storage.add_to_tail(item)

        

    def get(self):
        # Note:  This is the only [] allowed
        # list_buffer_contents = [value for value in self.storage]

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
