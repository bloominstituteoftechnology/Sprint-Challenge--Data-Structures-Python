from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Add to tail if not at full capacity
        if self.storage.length < self.capacity:
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        else:
            # replace value
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next


    def get(self):
        ring_buffer = []
        node = self.storage.head
        while node:
            ring_buffer.append(node.value)
            node = node.next
        return ring_buffer


if __name__ == '__main__':

    buffer = RingBuffer(3)

    print(buffer.get())   # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    print(buffer.get())   # should return ['a', 'b', 'c']

    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    print(buffer.get())   # should return ['d', 'b', 'c']

    buffer.append('e')
    buffer.append('f')

    print(buffer.get())   # should return ['d', 'e', 'f']