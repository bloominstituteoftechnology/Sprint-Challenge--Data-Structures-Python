class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        # returns the node's data
        return self.value

    def get_next(self):
        # returns the Node that this Node is pointing at
        return self.next_node

    def set_next(self, new_next):
        # sets this node's 'next' reference to the 'new_next'
        self.next_node = new_next

# node = Node(1)
# node.set_next(Node(2))
# node.get_next().set_next(Node(3))
# node.get_next().get_next.set_next(Node(4))


class LinkedList:
    def __init__(self):
        # the first Node in the linked list
        self.head = None
        # the last Node in the linked list
        self.tail = None

    def add_to_tail(self, value):
        # adds data to the end of the linked list
        # wrap the data in a node instance
        new_node = Node(value, None)

        # what about the empty case, when both self.head = None
        if not self.head:
            # list is empty
            # update both the head and tail to point to the new node
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node


    def remove_head(self):
        # removes the Node that self.head is referring to and returns the
        # . Node's data
        if not self.head:
            return None
        # if head has no next, there is a single element in the linked list
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        value = self.head.get_value()
        # set the head reference to teh current head's next node in the list
        self.head = self.head.get_next()
        return value
    
    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value
    

    def contains(self, value):
        if not self.head:
            return False
        
        # get a reference to the node we're currently at; update this as we go
        current = self.head
        # check to see if we're at a valid node
        while current:
        # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        
        return False
    
    
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value
