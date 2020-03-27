from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):
        if len(self.storage) == self.capacity:
            if self.oldest == None:
                self.oldest = self.storage.tail
            self.oldest.value = item
            self.oldest = self.oldest.prev
        else:
            self.storage.add_to_head(item)
            if len(self.storage) == self.capacity:
                self.oldest = self.storage.tail
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.tail 
        while node != None:
            list_buffer_contents += [node.value]
            node = node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#         self.index = 0
#         self.update_index = 0

#     def append(self, item):
#         if len(self.storage) == self.capacity:
#             if self.update_index >= len(self.storage):
#                 self.update_index = 0
#             self.storage[self.update_index] = item
#         else:
#             self.storage.append(item)
            

#     def get(self):
#         return self.storage