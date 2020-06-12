from singly_linked_list import Node, LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        val = None
        if self.size > 0:
            self.size -= 1
            val = self.storage.remove_head()
        return val
