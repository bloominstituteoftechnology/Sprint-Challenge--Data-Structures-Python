from doubly_linked_list import DoublyLinkedList

# Look to see whether list has reached full capacity
# if so - replace the current item with the new item
# move current item to next item in list
# if current item = tail, next value is head
# if not at capacity then add to end of storage
# if the storage had no items then set current item to new item
# add node data to list and move pointer

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == len(self.storage):
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            if len(self.storage) == 1:
                self.current = self.storage.head

    def get(self):
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass