import sys

from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.dll = DoublyLinkedList()

    def push(self, value):
        if value != None:
            self.dll.add_to_tail(value)
            self.size += 1

    def pop(self):
        try:
            val = self.dll.tail.value
            self.dll.remove_from_tail()
            self.size -= 1
            return(val)
        except:
            print('There are no values')

    def len(self):
        return self.size
