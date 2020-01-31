from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.length = 0

    def append(self, item):
        if (self.length == self.capacity):
            if (self.current.next is not None):
                self.current.value = item
                self.current = self.current.next
            elif(self.current.next is None):
                self.storage.tail.value = item
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            self.length += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while (current is not None):
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
