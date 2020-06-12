from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if capacity is not full
        if self.storage.length < self.capacity:
            #add the item to the the tail
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.storage.length == self.capacity: #if the storage is full
            self.current.value = item
        # replace the oldest item in buffer
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next




    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        # if current is true then append the node values into the list
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents