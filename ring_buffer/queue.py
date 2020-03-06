from doubly_linked_list import DoublyLinkedList
"""
Data Structure where You add data in and remove data out 
--> data collection
FIFO first in first out 
think of a line
first piece of data in the queque is the first piece out 
"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

#push 
    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1
        
            
        
#pop
#removing from wrong place 
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        
        else: 
            return None

    def len(self):
        return self.size


