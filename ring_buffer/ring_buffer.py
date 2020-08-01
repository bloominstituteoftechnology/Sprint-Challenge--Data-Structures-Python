from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            # remove item from head
            remove_item = self.storage.head
            self.storage.remove_from_head()
            #append new item to tail
            self.storage.add_to_tail(item)
            if remove_item == self.current:
                self.current = self.storage.tail

        # elif?
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        list_contents = []

        if self.storage.length == 0:
            return 'empty buffer'

        active_node = self.current
        # append new value to buffer
        list_contents.append(active_node.value)
        
        if active_node.next:
            next_node = active_node.next
        else:
            next_node = self.storage.head
        
        while next_node != active_node:
            list_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_contents