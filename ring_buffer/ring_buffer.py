from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #check to see if list is at capacity
        # if not
        if self.capacity > self.storage.length:
            #add item to tail
            self.storage.add_to_tail(item)
            # if an item is already there, then replace it with curent value
            if self.storage.length == 1:
                self.current = self.storage.head
        
        else:
            self.current.value = item

            if self.current is not self.storage.tail:
                self.current = self.current.next
            else:
                self.current = self.storage.head

        

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


'''class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
'''