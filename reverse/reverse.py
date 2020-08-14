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

    def reverse_list(self, node, prev): 
        #set prev to none
        #make new node reversal point head
        self.prev = None
        node = self.head 
        
        #while theres something in the list
        while(node is not None): 
            #alias the next node as next
            next = node.next_node
            #link the new head to the next node as a prev
            node.next_node = self.prev 
            #make the prev the new head
            self.prev = node
            #move along to each 
            node = next

        #use this to make it none after while? unsure if is the best, but works
        self.head = self.prev 

    #def reverse_list(self, node, prev=None):
    #    if node:
    #        self.reverse_list(node.next_node, node)
    #        node.set_next(prev)
    #    else:
    #        self.head = prev