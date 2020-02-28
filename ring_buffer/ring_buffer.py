from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the storage is not full then add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            # updates current storage
        elif self.storage.length == self.capacity:
            # if the storage is full remove the head and get more space since head is the oldest and you get more room
            current_head = self.storage.head
            self.storage.remove_from_head()
            # then add the item to the tail (tail takes in the newest items, head gets rid of oldest items)
            self.storage.add_to_tail(item)
            if current_head == self.current:
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
