from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # shouln't be able to append to zero capacity
        if self.capacity <= 0:
            return
        
        # should replace oldest element when full capacity
        if len(self.storage) == self.capacity:
            if not self.oldest:
                self.oldest = self.storage.tail
            
            self.oldest.value = item
            self.oldest = self.oldest.prev
        else:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # empty buffer 
        if len(self.storage) <= 0:
            return list_buffer_contents

        current = self.storage.tail
        list_buffer_contents.append(current.value)

        while current.prev:
            current = current.prev
            list_buffer_contents.append(current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
