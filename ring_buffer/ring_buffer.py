from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        
        # must be size of capcacity
        self.capacity = capacity
        self.storage = [None] * self.capacity

        # moving index, must init
        self.index = -1

    def append(self, item):
        
        self.index += 1
        print(item, self.index, len(self.storage))
        if self.index == len(self.storage):
            self.index = 0
        self.storage[self.index] = item


    def get(self):
        return [n for n in self.storage if n is not None]
