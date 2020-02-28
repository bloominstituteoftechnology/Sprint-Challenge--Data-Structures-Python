from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If nothing in storage yet
        if self.storage.head == None and self.capacity > 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        # Here are two scenarios in which we are at capacity
        # First, when current is at the end of the list:
        elif self.storage.length == self.capacity and self.current == self.storage.tail:
            # We replace the head value with the new value
            self.storage.head.value = item
            # Then we move current back to the start of the list
            self.current = self.storage.head
        # Second, when current is somewhere else in the list:
        elif self.storage.length == self.capacity:
            # Replace the next value with the new value
            self.current.next.value = item
            # Increment current
            self.current = self.current.next
        
        # Otherwise, we can just add the item to tail and increment current
        else:
            self.storage.add_to_tail(item)
            self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        # If list isn't empty, we'll do some stuff
        if self.storage.head != None:
            # Start out with head
            item = self.storage.head
            # and append value to list
            list_buffer_contents.append(item.value)
            # Now iterate through list until you hit the end
            while item.next:
                # Increment item
                item = item.next
                # Append item to list
                list_buffer_contents.append(item.value)

        # If list is empty, all we'll do is return the empty list
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
