from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If it's empty there is room
        # if self.storage.head == self.storage.tail
        # Make sure there's room in the RingBuffer Inn
        if self.storage.length < self.capacity:
            # Add the new element to the tail (FIFO)
            self.storage.add_to_tail(item)
            # Update the pointer to the oldest which becomes the head
            self.current = self.storage.head
        # The buffer is full remove the oldest one (at the head)
        else:
            # Get the oldest (head) element
            #oldest = self.storage.head
            # and remove it
            self.storage.remove_from_head()
            # Add the new item to the tail
            self.storage.add_to_tail(item)
            # Check the number of item
            if self.storage.length == 1:
                # Only one item so the new item is also the head
                self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
