from doubly_linked_list import ListNode, DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

        # Don't do this!
        # for i in range(capacity):
        #     self.storage.add_to_tail(None)
        #     self.current = self.storage.head

    def append(self, item):
        # Allocate space, if necessary
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            # Initialize the "current" pointer on the
            # first wrap-around
            if self.current == None:
                self.current = self.storage.head
                print("Self.current.value ", self.current.value)
            # Store the item at the current spot.
            # (overwrite anything that exists)
            self.current.value = item
            # Move the "current" pointer forward.
            # (wraps around the end of the list)
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        parse_pointer = self.storage.head  # Always start at the head

        while parse_pointer:
            if parse_pointer.value != None:
                # Add all non-null values to the list buffer response
                list_buffer_contents.append(parse_pointer.value)
            parse_pointer = parse_pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
