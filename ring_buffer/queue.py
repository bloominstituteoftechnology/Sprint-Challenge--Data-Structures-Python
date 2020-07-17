from singly_linked_list import CircularLinkedList

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = CircularLinkedList()                
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.__len__() > 0:
            self.size -= 1
            return self.storage.remove_head()