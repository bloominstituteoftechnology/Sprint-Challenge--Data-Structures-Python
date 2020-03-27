from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None 
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Current will act as a pointer
        # IF the ring still has room, do this
        if self.storage.length < self.capacity:
            #Add the new item to the tail
            self.storage.add_to_tail(item)
            #Set current to equal the tail
            self.current = self.storage.tail
        
        # If the current pointer is = to the tail
        elif self.current == self.storage.tail:
            #Set the head to the new item
            self.storage.head.value = item
            #Move the pointer to the head
            self.current = self.storage.head
        
        #Finnaly when the pointer is anywhere but the tail and the list is full
        else:
            #set the next item past the pointer = to the item
            self.current.next.value = item
            #Move the pointer to the next one
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #Set a node at the head of the ring. 
        node = self.storage.head
        #Loop through the ring and add the items to the list
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
