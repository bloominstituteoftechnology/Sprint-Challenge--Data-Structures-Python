from doubly_linked_list import DoublyLinkedList

#first in, circular first out with fixed size 
#queue us FIFO so use that? 
#When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #add an element over writing the oldest one 
        #   if it is not full...
        if self.storage.length < self.capacity:
            #add item to tail end of buffer
            self.storage.add_to_tail(item)
            #set the tail to current node position
            self.current = self.storage.head

        #if it is full 
        elif self.storage.length == self.capacity:
            #remove from head 
            self.storage.remove_from_head()
            #add new item to the tail 
            self.storage.add_to_tail(item)
            #current node becomes head, which makes it the oldest item in buffer
            self.storage.head ==  self.current
            #tail becomes current which makes it the newest item in tail 
            self.current = self.storage.tail
        else:
            #if empty 
            if self.storage.length is 0:
                # add item to the head 
                self.storage.add_to_head(item)
                #set head to current 
                self.current = self.storage.head


    def get(self):
    #     # Note:  This is the only [] allowed
        list_buffer_contents = []
        #creata variable for head 
        current_position = self.storage.head

        #while there self.storage.head isn't None
        while current_position is not None:
            #add value to array using method above
            list_buffer_contents.append(current_position.value)
            #the next node becomes current 
            current_position = current_position.next

        return list_buffer_contents




# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass
    
    # self.storage[self.current] = item
        # self.current += 1
        # if self.capacity == self.capacity-1:
        #     self.current = 0
        # # self.storage.add_to_head(self.current)
        # return self.storage

    def append(self, item):
        pass

    def get(self):
        pass
