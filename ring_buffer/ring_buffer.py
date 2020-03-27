from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # head is oldest info
        

        # if empty list
        if self.current == None:
            self.storage.add_to_tail(item)
            cur = self.storage.head
            self.current = cur.next
        
        # if list is at capacity
        elif len(self.storage) == self.capacity:

            # replace value 
            self.current.value = item
            
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        
        # list is not at capacity
        else:
            self.storage.add_to_tail(item)
            if len(self.storage) == self.capacity:
                self.current = self.storage.head



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # cursor
        cur = self.storage.head

        # iterate through the dll
        while cur.next:
            # if value is not none put it in the list
            if cur.next:
                list_buffer_contents.append(cur.value)
            cur = cur.next

        # add last value
        list_buffer_contents.append(cur.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
