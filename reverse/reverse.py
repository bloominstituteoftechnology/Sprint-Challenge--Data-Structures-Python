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
        current = node
        if current is None:                         # checking to see if node called in the parameters is none 
            return None                             # if it is none return none
        if current.get_next() ==  None:             # checking to see if the next node in the list none 
            self.head = current                     # if the next node is none. Set self.head to be the current node 
            self.head.next_node = prev              # setting next_node pointer at the previous node 
            return                                  #this returns the function and ends it.
        self.reverse_list(current.get_next(), node )# inputing the next node as the argument for node and the current node as the argument for previous.
        current.next_node = prev                    # this flips the pointer from the current next node to the previous node. 

"""
1->2->3->None
```
would become...
```
3->2->1->None
"""
    # def reverse_list(self, node, prev):
    #     prev_n = prev                    # set previous to be none
    #     c_n = self.head                  # current is == self.head
    #     next_node = None

    #     while c_n is not None:           # while the current head is not == to none 
    #         next_node = c_n.next_node    # change the value of the current head 
    #         c_n.next_node = prev_n       # compare the current and previous node
    #         prev_n = c_n                 # previous = current 
    #         c_n = next_node              # current = next 
    #     self.head = prev_n               # self.head is continually becoming the previous value 


    # def reverse_list(self, node, prev): # c_head = current head, n_head = new head, f_head = future head 
        # if node is None: 
        #     return None
        # if node.next_node is None:                 #this is pointing to none return node 
        #     return node
        # c_head = node                              # created a variable called current head and assigned it to Node 
        # n_head = c_head.next_node
        # f_head =self.reverse_list(n_head, None)
        # n_head.next_node = c_head
        # n_head = f_head
        # self.head = n_head
        # return n_head 


