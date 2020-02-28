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
            # oldest item's position is self.current modulo 3
            for i in range(self.current % self.capacity):
                replacing = replacing.next
            replacing.insert_before(item)
            # set head and tail of DLL
            if replacing == self.storage.head:
                self.storage.head = replacing.prev
            if replacing == self.storage.tail:
                self.storage.tail = replacing.prev
            replacing.delete()
        self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current.next:
            list_buffer_contents.append(current.value)
            current = current.next
        # append last item
        list_buffer_contents.append(current.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None for x in range(capacity)]
        self.current = 0
        self.capacity = capacity

    def append(self, item):
        self.storage[self.current % self.capacity] = item
        self.current += 1

    def get(self):
        return [x for x in self.storage if x != None]
