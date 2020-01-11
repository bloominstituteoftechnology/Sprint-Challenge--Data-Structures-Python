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
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
        # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
            # if we've gotten here, then the target node isn't in our list
        return False



    # added this to  check output ordering
    # METHOD is adding to HEAD, will push things left, other implementations add to tail
    def print_list(self):
        arr = []
        curr_node = self.head   # start from left
        while curr_node:  # same as while curr_node is not None:
            arr.append(curr_node.value)
            print("\t node: ", curr_node.value)
            curr_node = curr_node.next_node
        print('Adding to head, linked list is : ', arr)    


    def reverse_list(self):
        prev_pointer = None
        current = self.head

        while current:
            next_node = current.get_next()
            current.set_next(prev_pointer)
            prev_pointer = current
            current = next_node
 
        self.head = prev_pointer
    


list1 = LinkedList()
list1.add_to_head(1)
list1.add_to_head(2)
list1.add_to_head(3)

list1.print_list()

list1.reverse_list()
list1.print_list()

