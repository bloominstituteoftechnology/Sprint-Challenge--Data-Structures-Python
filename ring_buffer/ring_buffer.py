from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #check if full
        if self.capacity == len(self.storage):
            #if full replace the item with the new one
            self.current.value = item
            #check if next is the tail
            if self.current == self.storage.tail:
                #the next is head
                self.current = self.storage.head
            else:
                self.current = self.current.next
        #if not full 
        else:
            #add to storage
            self.storage.add_to_tail(item)
            #if storage empty
            if len(self.storage) == 1:
                #set current to new item 
                self.current = self.storage.head
    
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        new_item = self.storage.head
        while new_item is not None:
            #add the value to list buffer array
            list_buffer_contents.append(new_item.value)
            #move pointer to next
            new_item = new_item.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
