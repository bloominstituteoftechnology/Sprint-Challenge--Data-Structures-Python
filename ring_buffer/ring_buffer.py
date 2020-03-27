from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.storage.length >= self.capacity:
            lru = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if lru == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        node = self.storage.head
        
        while  node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents
    
    
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# print("Appending: a, b, c")
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# print("Appending: 'd'; 'd' should overwrite 'a'")
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# print("Appending 'e', 'f'; Both should overwrite 'b' & 'c' respectively")
# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
