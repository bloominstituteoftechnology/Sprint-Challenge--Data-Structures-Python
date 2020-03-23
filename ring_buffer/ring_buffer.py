from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __str__(self):
        return print(self.storage)

    def append(self, item):
        print(len(self.storage))

        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            print(f'storage after add to tail {self.storage}')
        else:
            next_current = self.current.next
            self.current.insert_after(item)
            self.storage.delete(self.current)
            print(f'storage after delete {self.storage}')
            self.current = next_current
            print(f'self.current after delete  {self.current.value}')



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        counter = 0
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents


rb = RingBuffer(5)
rb.append('a')
rb.append('b')
rb.append('c')
rb.append('d')
rb.append('e')
rb.append('f')
rb.append('g')
# print(rb)
print(rb.get())


# ----------------Stretch Goal-------------------




class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
