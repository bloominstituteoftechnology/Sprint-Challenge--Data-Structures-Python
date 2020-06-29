class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_node(self):
        return self.node

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
        
    def display(self):
        elements = []
        current = self.head
        while current != None:
            elements.append(current.value)
            current = current.get_next()
        print(elements)

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
        marker = self.head
        nextNode = None
        prev = None
        # assume prev is None already?
        #check if next is not None

        # iterative solution
        while marker is not None:
            #grab node next to marker
            nextNode = marker.next_node
            #overwrites next_node connection to prev
            marker.next_node = prev #prev == None first run
            #updates prev 
            prev = marker
            #sets marker as nextNode
            marker = nextNode
            
        self.head = prev
    
        #recursive

        # if not node:
        #     self.head = prev
        #     return 
        # else:
        #     nextNode = node.next_node
        #     node.next = prev
        #     self.reverse_list(nextNode, node)
       



ll = LinkedList()
ll.add_to_head(5)
ll.add_to_head(4)
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)
ll.display()
ll.reverse_list(ll.head, None)
ll.display()