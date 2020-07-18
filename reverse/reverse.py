class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverseUtil(self, curr, prev): 
          
        # If last node mark it head 
        if curr.next_node is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next_node = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next_node
  
        # And update next  
        curr.next_node = prev 
      
        self.reverseUtil(next, curr) 

    def reverse_list(self, node, prev):
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 
