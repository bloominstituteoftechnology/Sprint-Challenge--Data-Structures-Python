from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if ths storage (doublylinkedlist) is not full then we will add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # updating the current storage
        elif self.storage.length == self.capacity:
            remove_head = self.storage.head
        # if the storage is full, remove the head and get more space because the head is the oldest and we need more room
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
        # then add the item to the tail (tail takes in the newest items, head gets rid of oldest items)
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

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
    # this loops through each node and appends the values
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
