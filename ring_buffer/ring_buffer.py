from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        print('capacity', self.capacity)
        self.current = self.storage.head
        print('current', self.current)
        while list_buffer_contents != self.capacity:
            if self.current.next:
                list_buffer_contents.insert(self.current.value)
                self.current = self.current.next

        return list_buffer_contents

cat = RingBuffer(5)
cat.append('a')
cat.append('b')
cat.append('c')
cat.append('d')
print(cat.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
