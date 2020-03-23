from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:  # check to see if capacity is full
            # if capactiy is not full add item to the tail
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.storage.length == self.capacity:  # if capacity is full
            self.current.value = item
            # replace oldest item in buffer with the newest item being inserted
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        # elif self.storage.length == self.capacity:
        #     old_head = self.storage.head
        #     self.storage.remove_from_head()
        #     self.storage.add_to_tail(item)
        #     if old_head == self.current:
        #         self.current = self.storage.tail

            # # self.current = item
            # # self.storage.remove_from_head()
            # # self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current:  # if this is true, loop through, add contents to list_buffer
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
