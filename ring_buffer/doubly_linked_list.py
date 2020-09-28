class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
        
    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        value = self.head.value
        
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            self.tail = None
            self.head = None
            
            self.length = 0
            
            return value
        else:
            new_head = self.head.next
            new_head.prev = None
            
            self.length -= 1
            self.head = new_head
            
            return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        
        self.length += 1
        
        has_no_items = self.head is None and self.tail is None
        
        if has_no_items:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            
            new_node.prev = self.tail
            
            self.tail = new_node

    def remove_from_tail(self):
        has_no_items = self.head is None and self.tail is None
        has_one_item = self.head == self.tail
        
        value = self.tail.value
        
        if has_no_items:
            return None
        
        if has_one_item:
            self.tail = None
            self.head = None
            self.length = 0
            
            return value
        else:
            previous_node = self.tail.prev
            previous_node.next = None
            
            self.length -= 1
            self.tail = previous_node
            
            return value

    def move_to_front(self, node):
        previous_node = node.prev
        next_node = node.next
        
        if node.prev == None:
            return None
        
        if node.next == None:
            previous_node.next = None
            
            self.tail = previous_node
            self.length -= 1
            self.add_to_head(node.value)
        else:
            previous_node.next = next_node
            next_node.prev = previous_node
            
            self.length -= 1
            self.add_to_head(node.value)

    def move_to_end(self, node):
        previous_node = node.prev
        next_node = node.next
        
        if node.next == None:
            return None
        
        if node.prev == None:
            next_node.prev = None
            
            self.head = next_node
            self.length -= 1
            self.add_to_tail(node.value)
        else:
            previous_node.next = next_node
            next_node.prev = previous_node
            
            self.length -= 1
            self.add_to_tail(node.value)

    def delete(self, node):
        previous_node = node.prev
        next_node = node.next
        
        value = node.value
        
        if node.prev == None:
            self.remove_from_head()
            
            return value
        
        if node.next == None:
            self.remove_from_tail()
            
            return value
        else:
            previous_node.next = next_node
            next_node.prev = previous_node
            
            self.length -= 1
            
            return value

    def get_max(self):
        current_node = self.head
        max_value = 0
        
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
                
            current_node = current_node.next
        return max_value