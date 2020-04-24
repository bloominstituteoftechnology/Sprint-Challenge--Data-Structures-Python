from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    """
    The test for this actually conflicts with the spec. The spec states "A ring buffer is a 
    non-growable buffer with a fixed size." But the test is testing that the size changes. Wouldn't
    a better approach be to initialize the storage with a list of nodes with a value of None?
    Then you can roll through them and set the value to whatever it should be. This way the expense
    of creating the ring buffer comes at the time of creation, not at the time of use. 
    """
    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            return
        else:
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.advance()

    def advance(self):
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        buffer = [item for item in self.storage if item is not None]
        return buffer
