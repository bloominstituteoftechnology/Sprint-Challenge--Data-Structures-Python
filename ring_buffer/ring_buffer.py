from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            return
        if len(self.storage) >= self.capacity:
            if self.current != self.storage.tail:
                self.current.next.value = item
                self.current = self.current.next
            else:
                self.current = self.storage.head
                self.current.value = item
        else:
            self.storage.add_to_tail(item)
            self.current = self.current.next

    def get(self):
        list_contents = []

        current = self.storage.head
        while current:
            list_contents.append(current.value)
            current = current.next

        return list_contents