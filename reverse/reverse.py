class Node:# initialize class
    def __init__(self, value=None, next_node=None):
        # this is the value of the linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        # returning the value of our (current)node
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # we passing the next node of our self to a new node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # we are reffering to the head of the list equal to None
        self.head = None

    def add_to_head(self, value):
        # we are wrapping the value(argument, number, target) in a node
        node = Node(value)
        # we check if the head it is None
        if self.head is not None:
            node.set_next(self.head)
        # setting the head to a node
        self.head = node

    def contains(self, value):
         # we check if the head it is None and return False
        if not self.head:
            return False
        # refering to the current node position
        current = self.head
        # we check to see if the node is valid
        while current:
            # if the current value that we are searching matches with the value return it to True
            if current.get_value() == value:
                return True
            # at this point update our current node to the next node
            current = current.get_next()
        # if we reach this point then value we are searching is not in the list and we return to False
        return False

    def reverse_list(self, node, prev):
        # check to see if node is None and return to None
        if node is None:
                return None
        # see if the next node of node is None
        if node.next_node is None:
            # if yes,set the head pointer to be this node
            self.head = node
            # if no pass the next node of the node to previous
            node.next_node = prev
            return None
        temp = node.next_node
        node.next_node = prev
        # set the reversing to the head of our node
        self.reverse_list(temp,node)

        
            
     
