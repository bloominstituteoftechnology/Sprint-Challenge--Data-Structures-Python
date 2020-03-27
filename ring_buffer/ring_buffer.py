from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item) # Keep adding to tail until full
            self.current = self.storage.head # Keep current at head
        else:
            self.current.value = item # Set current node to item
            if self.current.next: # Go to next node if one exists
                self.current = self.current.next 
            else: # Return to head if at tail (next = None)
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head # Start at head
        while node: # Until node is None
            list_buffer_contents.append(node.value) # Add node's value
            node = node.next # Go to next node

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pos = 0
        self.storage = [None] * self.capacity # Fill list with None's 

    def append(self, item):
        self.storage[self.pos] = item # Set position to item
        self.pos = (self.pos + 1) % self.capacity # Add to position, resetting to 0 if at end

    def get(self):
        if None in self.storage:
            return self.storage[:self.storage.index(None)] # Get up to first None
        else:
            return self.storage # If all full, return list