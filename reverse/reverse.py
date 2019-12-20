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

  def reverse_list(self):
    # TO BE COMPLETED
    # Tracks for an empty list (line 22 test)
    if self.head is None:
        return None

    # Checks for single item on the list (line 26 in test)
    if self.head.next_node is None:
        return self.head.value

    # Longer reverse test
    # Begins with second item (current), next set item behind current to current's next by changing the side the value is located
    # If continued, at the end the item behind the last has the history of everything be added after it,
    # making the last item the front(head) then sets last item as head

    current = self.head.next_node # Begins on the second item
    node_behind = self.head # Item behind the current set to start

    while current is not None:
        future_current = current.next_node # Store the item that will be checked thru next loop
        current.set_next(node_behind) #  Now instead of N(5) -> N(4), it is N(4) -> N(5) has swapped
        node_behind = current # Shift over one in the list
        current = future_current # Same as above
    self.head = node_behind # Once we hit the end, the node_behind becomes the last item  edited in the list, which now has all reversed

test_list = LinkedList()
test_list.add_to_head(1)
test_list.add_to_head(2)
test_list.add_to_head(10)
test_list.reverse_list() 