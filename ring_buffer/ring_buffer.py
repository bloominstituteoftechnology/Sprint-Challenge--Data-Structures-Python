from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.capacity == self.storage.length:
            delete_this = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if delete_this == self.current:
                self.current = self.storage.tail



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        start_node = self.current
        list_buffer_contents.append(start_node.value)

        if start_node.next is not None:
            next_node = start_node.next
        else:
            next_node = self.storage.head

        while next_node != start_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current_index = 0

    def append(self, item):
        self.storage[self.current_index] = item
        #increment index
        self.current_index += 1
        #if index is at capacity, move it back to the beginning
        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self):
        return [i for i in self.storage if i]
