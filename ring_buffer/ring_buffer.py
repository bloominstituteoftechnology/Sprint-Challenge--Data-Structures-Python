from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            if self.current.next:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next
            else:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

# # ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
