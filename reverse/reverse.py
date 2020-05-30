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
        if node.next != None:
            self.reverse_list(node.next, prev = None)
        node.next = prev

    
       
    def printNode(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()



myList = LinkedList()
myList.add_to_head(1)
myList.add_to_head(2)
myList.add_to_head(3)
myList.add_to_head(4)
myList.printNode()



# Sample codes 
#    
#       def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         node = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return node
#----------------------------------------------

    # def reverseList(self, head):
    #     return self._reverse(head)

    # def _reverse(self, node, prev=None):
    #     if not node:
    #         return prev
    #     n = node.next
    #     node.next = prev
    #     return self._reverse(n, node)
    #----------------------------------------------

#     def reverse_list(self, node, prev):
#         if not node:
#             return prev
        
#         curr, node.next = node.next, prev
#         return self.reverse_list(curr, node)
#-------------------------------------------------------

# def reverse_recursively(self, node, pre=None):
#     if node.next != None:
#         self.reverse_recursively(node.next, pre=node)
#     node.next = pre
#------------------------------------------------------
# def reverse_list(self,node):
#      if node is None:
#          return //list is empty
#      elif node.next is None:
#         self.head = node // changing the head to last node after reversal
#         return
#      else:
#         reverse_list(node.next) //call the function recursively until the end of the list
#         node.next.next = node //reverse the link
#         node.next = None
# ----------------------------------------------------

    
    # def reverse_list(self,node):
    #     if node.get_next() == None:
    #         self.head = node
    #         return
    #     self.reverse_list(node.get_next())
    #     temp = node.get_next()
    #     temp.set_next(node)
    #     node.set_next(None)