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
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = new_node
            self.head = new_node

    
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        #check for emtpy list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            

    
    def remove_from_tail(self):
        # Get the value of tail
        value = self.tail.value
        #Use your delete method to remove that value
        self.delete(value)
        #return that value
        return value

    
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)


    
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    
    def delete(self, node):
        self.length -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
    
    def get_max(self):
        value = self.head.value
        current = self.head

        while current is not None:
            if current.value > value:
                value = current.value
            current = current.next
        return value





class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentValue = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check for capacity value
        if len(self.storage) < self.capacity:
            # if less, add to this list
            self.storage.add_to_tail(item)
            # keep that current value
            self.currentValue = self.storage.tail
        else: 
            # the capcity is equal to the currentValue
           if not self.currentValue.next:
            self.currentValue.value = item
            self.currentValue = self.storage.head
            else: 
            #this is where we'll have to figure out a way to replace
            #the last capcity value
            # and move the current over 
            self.currentValue.value = item
            self.currentValue = self.currentValue.next
            
            

    def get(self):
         ring_buffer_list = []
         
         node = self.storage.head
         while node:
             ring_buffer_list.append(node.value)
             node = node.next

         return ring_buffer_list