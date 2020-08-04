

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self) 
        if current_prev:
            current_prev.next = self.prev
            
            
    def delete(self):
        if self.prev:
            self.prev.next = self.next     
        if self.next:
            self.next.prev = self.prev    
            
            
            
class DoublyLinkedList:
         def __init__(self, node=None):
             self.head = node
             self.tail = node
             self.length = 1 if node is not None else 0
        
         def __len__(self):
            return self.length   
        
        
         def add_to_head(self, value):
             new_node = ListNode(value)
             
             self.length +=1
             
             if self.head:
                 new_node.next = self.head
                 self.head.prev = new_node
                 self.head = new_node
             else:
                
                self.head = new_node
                self.tail = new_node 
                
         def add_to_tail(self, value):
             new_node = ListNode(value, None, None)
             self.length  +=1
             
             if self.tail:
                 self.tail.next = new_node
                 new_node.prev = self.tail
                 self.tail = new_node
                 
             else:
                 self.head = new_node
                 self.tail = new_node             
                 
                 
         def remove_from_tail(self):
              value = self.tail.value
              self.delete(self.tail)
              return value        
          
          
         def delete(self,node):
             if not self.head:
                 return
             
             self.length -=1
             
             if self.head == self.tail:
                 self.head = None
                 self.tail = None
                 
             if node == self.head:
                 self.head = node.next
                 self.tail.next = None    
                 
                 
             if node == self.tail:
                  self.tail = node.prev
                  self.tail.next = None
             
             else:
                 value = node.value
                 node.delete() 
                 return value       
             
             
         def get_max(self):
             cur_node = self.head
             cur_max = self.head.value 
             if self.head == None:
                return None
            
             while cur_node is not None:
                if cur_node.value > cur_max:
                  cur_max =  cur_node.value
                cur_node = cur_node.next 
             return  cur_max       
             