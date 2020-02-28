from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check for length of storage is 0
        if len(self.storage) == 0:
            # If it is, than set new item to head
            self.storage.add_to_head(item)
            # And set current (aka oldest) to head
            self.current = self.storage.head

        # If storage is not full (is < capacity)
        elif len(self.storage) < self.capacity:
            # Add new item to the tail of the list
            self.storage.add_to_tail(item)

        # Else if storage is full capacity
        else:
            # Replace the value of current with new item
            self.current.value = item
            # Than check if next node to current (oldest) is None or Not
            # If node next to current is not None, than
            if self.current.next:
                # And move current to next node
                self.current = self.current.next
            # Else node next to current is None
            else:
                # Return the current back to head (aka beginning of the list)
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        dll = self.storage.head
        while(dll):
            list_buffer_contents.append(dll.value)
            dll = dll.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
