from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            remove_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        c = self.current

        list_buffer_contents.append(c.value)
        if c.next:
            n = c.next
        else:
            n = self.storage.head

        while n != c:
            list_buffer_contents.append(n.value)
            if n.next:
                n = n.next
            else:
                n = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
