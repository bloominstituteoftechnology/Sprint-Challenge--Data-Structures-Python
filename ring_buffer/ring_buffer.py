from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
            self.current = self.storage.head
        else:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
                self.current = self.storage.tail

            else:
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
                
        #     self.storage.add_to_tail(item)
        #     self.current.pre
        #     last_node = self.current
        #     self.current = last_node.next
        #     self.storage.delete(last_node)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        

        # TODO: Your code here
        for i in range(len(self.storage)):
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
