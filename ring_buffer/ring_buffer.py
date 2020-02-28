from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.storage.tail.prev.next = self.storage.tail

        else:
            flag = False
            if self.current == self.storage.head:
                flag = True
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            if flag:
                self.current = self.storage.head
                flag = False
            self.storage.head.prev = self.storage.tail
            self.storage.tail.next = self.storage.head
            self.storage.tail.prev.next = self.storage.tail
            self.storage.head.next.prev = self.storage.head
            self.storage.tail = self.storage.tail.next
            self.storage.head = self.storage.head.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.current is not None:
            list_buffer_contents.append(self.current.value)
        pointer = self.current
        while pointer.next != self.current and pointer.next is not None:
            pointer = pointer.next
            list_buffer_contents.append(pointer.value)
        return list_buffer_contents





# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
