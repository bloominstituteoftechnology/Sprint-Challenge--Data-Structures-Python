from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size
    def len(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = 0

    def append(self, item):
        if self.current < self.capacity:
            self.storage.add_to_head(item)
            self.current += 1
        if self.current > self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        s = Stack()
        s.push(self.storage.tail)
        while s.len() > 0:
            temp = s.pop()
            list_buffer_contents.append(temp.value)
            if temp.prev:
                # list_buffer_contents.append(temp.prev.value)
                s.push(temp.prev)
        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
