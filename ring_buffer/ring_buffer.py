from doubly_linked_list import DoublyLinkedList

# You want to define a buffer with a fixed size, 
# so that when it fills up, adding another element must overwrite the first (oldest) one. 
# This kind of data structure is particularly 
# useful for storing log and history information. 

# A ring buffer is a non-growable buffer with a fixed size. 
# A ring buffer is a buffer with a fixed size. When it fills up,
# adding another element overwrites the oldest one that was still being kept. 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        

# When the ring buffer is full and a new element is inserted, 
    def append(self, item):
        # base 
        node = self.storage.head

        """append an element at the end of the buffer"""
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # declare node 
            self.current = self.storage.head
        elif self.storage.length ==  self.capacity:
        # the oldest element in the ring buffer is overwritten with the newest element.
            oldest = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if oldest == self.current:
                # thats where current becomes new tail (is the head)
                self.current = self.storage.tail
                

            
            
        

           

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.current
        # TODO: Your code here
        list_buffer_contents.append(node.value)
        
                #now
        if node.next is not None:
            next_node = node.next
        else:
            next_node = self.storage.head
            
        # as long as there is a new node keep going until last
        while next_node != node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head
                
                 
            
            
            
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
