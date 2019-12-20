from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if at capacity
        if self.storage.length < self.capacity:
            # adding to tail and updating current position
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            # Removing head to make room
            drop_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            # Reset current position to tail
            if drop_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # establish starting point and appending
        first_node = self.current
        list_buffer_contents.append(first_node.value)
        # Moving to next node if first place is taken
        if first_node.next:
            seq_node = first_node.next
        # Add seq_node if there is not already a head
        else:
            seq_node = self.storage.head
        # Loop through each sequential node to append the values
        while seq_node != first_node:
            list_buffer_contents.append(seq_node.value)
            if seq_node.next:
                seq_node = seq_node.next
            else:
                seq_node = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
