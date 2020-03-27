from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
        else:
            self.storage.add_to_tail((item))
            self.storage.pop(0)
        

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
