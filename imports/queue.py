from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # A linked list gives O(1) time complexity here.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return len(self.storage)
