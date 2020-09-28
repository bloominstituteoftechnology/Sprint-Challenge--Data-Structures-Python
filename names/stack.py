from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # push means we are adding to the top/head of the DLL_Stack
        # we need to increment/increase size by 1
        self.size += 1
        # use add_to_head() to add the value in a new node
        # to the top/head of the DLL_Stack
        self.storage.add_to_head(value)


    def pop(self):
        # In pop function, we are subtracting/removing from the top/head of the DLL_Stack
        # if there is no node in storage
        if self.storage.head == None:
            # otherwise, return None
            return None

        else:
            # we will need to decrement/decrease size by 1
            self.size -= 1
            # use the function remove_from_head() to delete the last node added onto the DLL_Stack
            return self.storage.remove_from_head()
