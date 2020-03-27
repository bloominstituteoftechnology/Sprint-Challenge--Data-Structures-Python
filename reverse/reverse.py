class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution, and break my brain doing so...
        #If the pointer is none, return, this is for empty lists.
        if node == None:
            return
        #If the pointer next node is none, change the head of the list to the current pointer, this starts the reverasal
        elif node.get_next() == None:
            self.head = node
            return
        #Otherwise:
        else:
            #Recursion on the next item in the list
            self.reverse_list(node.get_next(), None)
            #Then get the next node, and set its next to the current one, this starts reversing the list
            node.get_next().set_next(node)
            #Then kill the old connection
            node.set_next(None)

# Lets pretend we have a list that goes 1->2->3->X, our goal is to get 3->2->1->X
# We have to do this recursivly, so ideally in just one pass
# We will want a pointer called current, that points at the head to start
# It checks the first 2 rules and finds neither will run, so then runs recursion on the next element.
# This continues until the pointer is pointing at 3. in which case it can run the 2nd argument, and turns 3 into the head
# then we go back up the call stack, where we grab the next node and set its next to the current node, in this case
# setting three to point to 2, and then we kill the connection of two pointing to three, finish the whole stack and its reversed!

#Lingering questions: why does reverse list call for previous? The tests never use it. 