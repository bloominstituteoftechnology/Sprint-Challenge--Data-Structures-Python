class Node:
    ########## INITIALIZE CONSTRUCTOR ##########
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
    ########## INITIALIZING THE HEAD ##########
    def __init__(self):
        self.head = None
        
        
    ########## NODE INSERTED IN FRONT ##########
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node



        ########## TRUE OR FALSE ##########
    def contains(self, value):
        if not self.head:
            return False
        
        
        ########## LOOPING THROUGH NODES ##########
        current = self.head

        while current:
            ########## MAKING SURE THIS IS THE NODE WE LOOKED FOR ##########
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    
    
    ########## 3 POINTERS == PREV/NULL == HEAD & NEXT ##########
    def reverse_list(self, x=None, y=None): 
        if self.head == None:
            return None
        current = self.head
        prev = None
        
        while current != None:
            next = current.next_node
            
            current.next_node = prev
            
            prev = current
            current = next
            
        self.head = prev
        
        
    ########## PRINTING LINKEDLIST ##########
    def print_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next_node

