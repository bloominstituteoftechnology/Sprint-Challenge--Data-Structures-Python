from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DoublyLinkedList(None)


    def append(self, item):
        size = self.dll.length
        if size < self.capacity:
            self.dll.add_to_tail(item)
        

        else:
            # find & replace the oldest node
            self.dll.replace_oldest(item)
            
            # self.dll.remove_from_head() #altered
            # self.dll.add_to_tail(item) #altered
          

    def get(self):
        lst = []
        checknode = self.dll.head
        while checknode is not None:
            lst = [*lst, checknode.item]
            checknode = checknode.next

        return list(lst)