from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # if list len is less than capacity
        if self.storage.length < self.capacity:
            # append item to storage
            self.storage.add_to_tail(item)
            # update current
            self.current = self.storage.tail

        # if buffer is full
        elif self.storage.length == self.capacity:
            # check if current is the tail
            if self.current == self.storage.tail:
                # overwrite head value
                self.storage.head.value = item
                # update current to head
                self.current = self.storage.head

            # we are somewhere else in the buffer
            else:
                # overwrite current's next value
                self.current.next.value = item
                # update current
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
