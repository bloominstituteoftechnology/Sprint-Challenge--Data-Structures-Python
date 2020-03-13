

from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # self.current stores the current oldest element
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next or self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage[self.oldest] = item
            self.oldest = 0 if self.oldest == self.capacity - 1 else self.oldest + 1

    def get(self):
        return list(filter(None, self.storage))

# The advantages of using a Python list instead of a linked list are:
# - accessing elements via indices is faster--const O(1) versus linear O(n) access time for linked lists

# The typical disadvantages of using a Python list instead of a linked list are:
# - fixed sizes rather than dynamic sizes
# - insertion and deletion are expensive

# The disadvantages normally found in arrays that are overcome with this arrangement are with runtime and space complexities. Typically, the runtime complexity of inserting or deleting a value at the front or in the middle of a Python list is linear O(n), since following values need to be shifted back. In this instance, however, since the inserted value replaces an existing value, no shifting of values due to insertion or deletion is needed. Additionally, since we know the length of the list from the outset, no additional space needs to be created for new elements. Since we know from the outset the capacity of the Ring Buffer, we don't have to worry about dynamic sizing.
