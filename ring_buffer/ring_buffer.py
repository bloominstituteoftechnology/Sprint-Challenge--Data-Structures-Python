from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            return

        if len(self.storage) == self.capacity:
            if self.current.next is None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.current = self.current.next
                self.current.value = item
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node:
            if not current_node is None and not current_node.value is None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents