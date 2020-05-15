from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # head is LRU

        # if list is empty
        if self.current == None:
            self.storage.add_to_tail(item)
            cur = self.storage.head
            self.current = cur.next

        # if list is full/ no empty spaces
        elif len(self.storage) == self.capacity:

            # replace value
            self.current.value = item

            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        # list is not completely full
        else:
            self.storage.add_to_tail(item)
            if len(self.storage) == self.capacity:
                self.current = self.storage.head



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # cursor
        cur = self.storage.head

        # iterate through dll
        while cur.next:
            # if not None, put it in the list
            if cur.next:
                list_buffer_contents.append(cur.value)
            cur = cur.next

        # add last value
        list_buffer_contents.append(cur.value)

        return list_buffer_contents
