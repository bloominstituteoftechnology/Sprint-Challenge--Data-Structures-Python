from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # If capacity is full
        if self.storage.length == self.capacity:
            # Replace oldest
            self.current.value = item
            # Reset oldest
            self.current = self.current.next
        else:
            # Add item to tail (most recent)
            self.storage.add_to_tail(item)
            
            if self.storage.length == self.capacity:
                self.storage.tail.next = self.storage.head
            else:
                # Reset oldeset
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        count = 0
        node = self.storage.head
        while count != self.storage.length:
            count += 1
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('s')
print(buffer.get())  # should return ['a', 'b', 'c']