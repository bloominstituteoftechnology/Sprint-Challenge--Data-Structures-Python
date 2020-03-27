from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):

        self.storage = DoublyLinkedList()
        self.capacity = capacity
        self.current_node = None

    def append(self, item):

        # normal insert 
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current_node = self.storage.tail

        
        else:

            if self.current_node == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current_node = self.storage.head
            else:
                self.storage.insert_after(self.current_node, item)
                self.current_node = self.current_node.next
                self.storage.delete(self.current_node.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        
        # must be size of capcacity
        self.capacity = capacity
        self.storage = [None] * self.capacity

        # moving index, must init
        self.index = -1

    def append(self, item):
        
        self.index += 1
        print(item, self.index, len(self.storage))
        if self.index == len(self.storage):
            self.index = 0
        self.storage[self.index] = item


    def get(self):
        return [n for n in self.storage if n is not None]
