from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('./doubly_linked_list')


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList() 
        self.ring_index = 0

    def append(self, item):
        
        if self.storage.length == 1:
           self.current = self.storage.head
        
        if len(self.storage) >= self.capacity:
           if self.current.next != None:
               self.current.value = item
               self.current = self.current.next 
               
           else:
               self.current.value = item
               self.current = self.storage.head  
               
        else:
            self.storage.add_to_tail(item)          

    def get(self):
        current_node = self.storage.head.next 
        
        contents = [self.storage.head.value]
        
        while current_node is not self.storage.head:
            
            if current_node is None:
                break
            contents.append(current_node.value)
            current_node = current_node.next
            
        return contents 