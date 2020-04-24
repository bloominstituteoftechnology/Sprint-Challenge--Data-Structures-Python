from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() == self.capacity:
            if self.current == None:
                self.current = self.storage.tail
            self.current.value = item
            self.current = self.current.prev
        else:
            self.storage.add_to_head(item)
            if self.storage.__len__() == self.capacity:
                self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        tail = self.storage.tail 

        while tail:
            list_buffer_contents.append(tail.value)
            tail = tail.prev

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
