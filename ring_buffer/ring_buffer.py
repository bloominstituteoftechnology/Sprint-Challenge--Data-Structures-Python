from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity: 
            if self.current_oldest.next is not None:
                self.current_oldest.value = item 
                self.current_oldest = self.current_oldest.next 
            else:
                self.current_oldest.value = item 
                self.current_oldest = self.storage.head 
    
        else: 
            self.storage.add_to_tail(item)
            self.current_oldest = self.storage.head

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents