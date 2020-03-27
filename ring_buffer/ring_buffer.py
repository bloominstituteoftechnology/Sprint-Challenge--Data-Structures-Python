from doubly_linked_list import DoublyLinkedList

# thought process:
# fixed capacity
# # the least recent element gets bumped when something new is added

# if we are at maximum capacity:
#     remove the stale item
#     add the new item
#     update self.current to be the new item 
# if we aren't at maximum capacity:
#     add the new item
    # be sure to update self.current to match the item

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        #if not at capacity:
        # add to the most recent
        # update current
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        # if at capacity
        # discard stale value
        # checking index of other values
        # moving through each of them
        # if the current value is the most recent, start at the beginning
        if len(self.storage) == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        


        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # starting at the stale item
        
        list_item = self.storage.head

        # as long as a list_item exists, append the list
        # if a list_item value is None, move on
        while list_item:

            if list_item.value == None:
                list_item = list_item.next
            else:
                list_buffer_contents.append(list_item.value)
                list_item = list_item.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
