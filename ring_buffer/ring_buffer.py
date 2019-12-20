from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == 0:
            if not self.storage.head:
                self.storage.add_to_tail(item)
            else:
                self.storage.head.value = item
        else:
            i = 0
            current_node = self.storage.head
            while i < self.current:
                if not current_node.next:
                    self.storage.add_to_tail(item)
                else:
                    current_node = current_node.next
                    i += 1
            current_node.value = item
        self.current += 1

        if self.current >= self.capacity:
            self.current = 0

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
print("===")
print(buffer.append('d'))
print(buffer.append('e'))
print(buffer.append('f'))
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
