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

        if self.storage.length == self.capacity:
            self.current.value = item
            
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head
        
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents