import sys

from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.dll = DoublyLinkedList()

    def enqueue(self, value):
        if value != None:
            self.dll.add_to_tail(value)
            self.size += 1

    def dequeue(self):
        try:
            val = self.dll.head.value
            self.dll.remove_from_head()
            self.size -= 1
            return(val)
        except:
            print('There are no values')

    def len(self):
        return self.size
