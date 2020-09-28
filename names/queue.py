from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size        

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.storage.head == None:
            return None

        else:
            # we need to decrement/decrease size by 1
            self.size -= 1
            # use remove_from_head() to delete the first node/the head
            return self.storage.remove_from_head()
