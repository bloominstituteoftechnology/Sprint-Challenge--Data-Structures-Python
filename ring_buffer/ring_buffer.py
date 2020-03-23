from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # we have to add the pieces to the end of the ring or the "tail" of the ring
        if self.storage < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # we have to update the current storage to accommadate the new item that we put in
        elif self.storage.length == self.capacity:
            remove_head = self.storage.head
        # if the ring reaches capacity, we must remove the head since its the oldest piece of info that we in the ring
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        c = self.current
        list_buffer_contents.append(c.value)
        if c.next:
            n = c.next
        else:
            n = self.storage.head

        while n is not c:
            list_buffer_contents.append(n.value)
            if n.next:
                n = n.next
            else:
                n = self.storage.head

        # this loop through each node and appends the values
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass