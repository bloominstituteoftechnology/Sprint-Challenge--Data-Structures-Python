from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Add if less than capacity
        if self.storage.length < self.capacity:
            # Add to tail
            self.storage.add_to_tail(item)
            # Update the current position
            self.current = self.storage.head

        elif self.storage.length == self.capacity:
            # remove head and add to tail
            remove_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            # Reset current position to tail
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # Start at the current node we are on and add the value to the list
        current_node = self.current
        list_buffer_contents.append(current_node.value)

        # If there is a node to the right then get next node
        if current_node.next:
            next_node = current_node.next

        # else start from beginning
        else:
            next_node = self.storage.head
        # Loop through entire list until we reach back to the current node that we started with
        while next_node != current_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
             # moves down list and when reaches end since no next then go back to the head.
                next_node = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
