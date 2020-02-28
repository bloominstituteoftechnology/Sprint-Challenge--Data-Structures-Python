from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # * if capacity has not been reached, add item to head and set current(oldest) val to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        # * when capacity is reached, if the current node is the tail, remove from tail and insert item to tail, set current to the item to the left of tail (oldest item is left of tail in this case)
        elif self.current == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.current.prev
        # *  when capacity is reached, if the current node is the head (all original entries have been replaced), if the current node is the head, remove the head and replace with new item, the current node then becomes the tail
        elif self.current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        # * edge case where capacity has been achieved but current node head or tail -- insert new item after the current value the item and then delete the current item, set the new current item to the previous
        else:
            self.current.insert_after(item)
            self.current.delete()
            self.current = self.current.prev

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.insert(0, current_node.value)
            if current_node.next is not None:
                current_node = current_node.next
            else:
                return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
