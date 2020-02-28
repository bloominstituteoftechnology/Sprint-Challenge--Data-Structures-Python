from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # total items ever appended
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            replacing = self.storage.head
            for i in range(self.current % self.capacity):
                replacing = replacing.next
            replacing.insert_before(item)
            temp = replacing
            if replacing == self.storage.head:
                self.storage.head = replacing.prev
            if replacing == self.storage.tail:
                self.storage.tail = replacing.prev
            temp.delete()
        self.current += 1

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
