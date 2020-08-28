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
        else:
            lru = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if lru == self.current:
                self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []

        cur = self.current
        list_buffer_contents.append(cur.value)

        if cur.next:
            next_node = cur.next
        else:
            next_node = self.storage.head

        while next_node is not cur:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents
