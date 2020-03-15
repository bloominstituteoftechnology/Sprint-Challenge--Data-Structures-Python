from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.length = 0

    def append(self, item):
        if self.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head    
            self.length += 1        
        elif self.length < self.capacity:
            self.storage.add_to_tail(item)
            self.length += 1
        elif self.current == self.storage.head:
            
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head.next
        elif self.current is self.storage.tail:

            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            print(self.current.value)
        else:
            #print(self.current.value)
            #self.current = self.current.next
            self.current.insert_before(item)
            delete = self.current
            self.current = self.current.next
            self.storage.move_to_end(delete)
            self.storage.remove_from_tail()


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        list_buffer_contents.append(self.storage.head.value)

        point = self.storage.head
        while point.next:
            point = point.next
            list_buffer_contents.append(point.value)

        return list_buffer_contents


# a = RingBuffer(3)
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.append(6)

# print(a.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.index = 0
        self.length = 0

    def append(self, item):
        if self.length == 0:
            self.list = [item]
            self.length += 1

        elif self.capacity > self.length:
            self.list = self.list + [item]
            self.length += 1

        elif self.index == self.capacity - 1:
            self.list[self.index] = item
            self.index = 0

        else:
            self.list[self.index] = item
            self.index += 1


    def get(self):
        pass
a = ArrayRingBuffer(4)
a.append(1)
a.append(2)
a.append(3)
a.append(5)
a.append(6)
a.append(7)
print(a.list)