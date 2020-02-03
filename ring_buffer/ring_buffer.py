from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
     # if storage is not full
        if self.storage.length < self.capacity:
            # add to tail
            self.storage.add_to_tail(item)
            # update current
            self.current = self.storage.head
        # if storage is full
        elif self.storage.length == self.capacity:
            # remove the head to free space since it is the oldest
            drop_head = self.storage.head
            self.storage.remove_from_head()
            # add item to tail (newest)
            self.storage.add_to_tail(item)
            # if we are at the head, set the current pos to the tail
            if drop_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        start = self.current
        list_buffer_contents.append(start.value)
        # loop through each node to append values
        if start.next:
                nxt = start.next
        else:
            nxt = self.storage.head

        while nxt != start:
            list_buffer_contents.append(nxt.value)
            if nxt.next:
                nxt = nxt.next
            else:
                nxt = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
