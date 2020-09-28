from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # no append for zero capacity
        if self.capacity <= 0:
            return

        # replace oldest when full capacity
        if len(self.storage) == self.capacity:
            if not self.oldest:
                self.oldest = self.storage.tail

            self.oldest.value = item
            self.oldest = self.oldest.prev
        else:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        buffer_contents = []

        # this is an empty buffer
        if len(self.storage) <= 0:
            return buffer_contents

        current = self.storage.tail
        buffer_contents.append(current.value)

        while current.prev:
            current = current.prev
            buffer_contents.append(current.value)

        return buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * 5

    def append(self, item):
        # will not be able to append to zero capacity
        if self.capacity <= 0:
            return

        # will add/replace item on buffer
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity

    def get(self):
        return [x for x in self.storage if x is not None]
