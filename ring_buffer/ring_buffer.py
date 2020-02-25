import sys
sys.path.append('C:\\Git\\python-lambda\Sprint-Challenge--Data-Structures-Python\\ring_buffer')
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        

    def append(self, item):
        #if empty storage
        #add to head to create list
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        elif self.storage.length == self.capacity:
            if self.current is None:
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            #storage full, current is tail, set to Head
            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = None

            #storage full, current is not tail or None
            else:
                self.current = self.current.next
                self.current.prev.delete()
                self.current.insert_before(item)
                

            
                
                
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current.next:
            list_buffer_contents.append(current.value)
            current = current.next
        list_buffer_contents.append(current.value)

        return list_buffer_contents

test_buffer = RingBuffer(5)
test_buffer.append('a')
test_buffer.append('b')
test_buffer.append('c')
test_buffer.append('d')
print(test_buffer.get())

test_buffer.append('e')
print(test_buffer.get())

test_buffer.append('f')
print(test_buffer.get())

test_buffer.append('g')
test_buffer.append('h')
test_buffer.append('i')

print(test_buffer.get())
test_buffer.append('j')
test_buffer.append('k')
print(test_buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
