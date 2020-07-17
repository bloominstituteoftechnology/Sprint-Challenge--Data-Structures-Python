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

     #  My addition so I could see the output       
    def printNode(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()

#  This is the answered I submitted on Friday, May 29th @ 11:59PM 

    # def reverse_list(self, node, prev):
    #     if node.next != None:
    #         self.reverse_list(node.next, prev = None)
    #     node.next = prev

#------------------------------------------------------------------

# This is the edit I made on Sunday, May 31th @ 5:47PM

# Steps:
# 1. Pass the head pointer to this method as node.
# 2. Check if the next node of node is None:
        # a) If yes, this indicates that we have reached the end of the linked list. Set the head  pointer to this node
        # b) If no, pass the next node of node to the reverse method
# 3. Once the last node is reached, the reversing happens.

    def reverse_list(self, node):
        if node.get_next()  == None:
            self.head = node
            return
        self.reverse_list(node.get_next())
        prev = node.get_next()
        prev.set_next(node)
        node.set_next(None)
   
# Sources:  
# 1. Lecture work - Doubly Linked Lists    
# 2. https://www.pythoncentral.io/reverse-singly-linked-list/
## NOTE: In order to solve this problem, I deleted 'prev' attribute from the 'reverse_list' class definition
   


#  Sample data
myList = LinkedList()
myList.add_to_head("first")
myList.add_to_head("second")
myList.add_to_head("third")
myList.add_to_head("fourth")
print("Original List:")
myList.printNode()
print("Reversed List:")
myList.reverse_list(myList.head)
myList.printNode()

