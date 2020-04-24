from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.count = 0

    def append(self, item):        
        #if there is enough capacity will add the item to the end
        
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        #if its full, it will overwrite the oldest item with a new one

        if self.storage.length == self.capacity:
            self.current.value = item

        #the most recently used item will be added to the head

        if self.current is self.storage.tail:
             self.current = self.storage.head
        else:
            self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # go throw each node and add the value to the buffer list
        pointer = self.storage.head
        while pointer:
            list_buffer_contents.append(pointer.value)
            pointer = pointer.next      

        # TODO: Your code here

        return list_buffer_contents
       
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
