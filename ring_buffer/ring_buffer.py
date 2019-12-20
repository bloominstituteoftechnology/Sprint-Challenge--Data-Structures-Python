from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        start_node = self.storage.head
        list_buffer_contents.append(start_node.value)
        while start_node.next is not None:
          start_node = start_node.next
          list_buffer_contents.append(start_node.value)
        return list_buffer_contents


buffer = RingBuffer(3)
print(buffer.storage.length)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.storage.length)
print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
