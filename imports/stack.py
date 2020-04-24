from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # A linked list gives O(1) time complexity here.
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        value = self.storage.remove_from_tail()
        return value

    def len(self):
        return len(self.storage)
