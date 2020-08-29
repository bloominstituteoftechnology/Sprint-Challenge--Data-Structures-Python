from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            old_node = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if old_node == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.length == 0:
            return 'Empty Buffer'

        node = self.current
        list_buffer_contents.append(node.value)    

        if node.next:
            next_node = node.next
        else:
            next_node = self.storage.head

        while next_node != node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head    

        return list_buffer_contents


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