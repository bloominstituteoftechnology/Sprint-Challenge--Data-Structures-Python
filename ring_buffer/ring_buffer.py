from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity: ## if the storage has capacity to add more 
            self.storage.add_to_tail(item)## add to end tail
            
        else:
            if self.current == None or self.current.next == None: ## if the current node is the last//no space
                self.current = self.storage.head
            
    ##Wrap the given value in a ListNode and insert it
    ##after this node. Note that this node could already
    ##have a next node it is point to.
            else: ## current to next 
                self.current = self.current.next
            
            self.current.value = item



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node != None:
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
