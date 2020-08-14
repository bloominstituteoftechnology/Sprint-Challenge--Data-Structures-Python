from Doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If storage is 0 change current to None
        if self.current is None:
            self.current = 0
        # If storage is full
        if self.storage.length == self.capacity:
            # Get Head
            node = self.storage.head

            if self.current > 0:
                # Go to the index we're replacing
                for _ in range(0, self.current):
                    node = node.next
            # Replace Value
            node.value = item
            # If we've reached overflow
            if self.current == self.capacity - 1:
                # Set back to None
                self.current = None
            else:
                # increment upwards
                self.current += 1
            # return
            return
        # add to tail
        self.storage.add_to_tail(item)
        pass

    def get(self):
        list_buffer_contents = []
        # get head

        # while head is none
        head = self.storage.head

        while head:
            # add to list
            list_buffer_contents.append(head.value)
            # go  to next
            head = head.next

        # return
        return list_buffer_contents
        pass
