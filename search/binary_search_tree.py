from queue import Queue

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):  # O(n)
    
    """
    The basic algorithm of Pre-order traversal is to visit the root, traverse the left subtree, then traverse the right subtree.
    Here, we're going to check the left or right, and recursively call the depth_first method, while passing in cb.
    cb is the closure (lambda in Python) that will hold on to the value so it can be used in the test file.
    """
    
    # Calling the callback with the current parent
    cb(self.value)
    
    # Traverse the left side
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    
    if self.right is not None:
      self.right.depth_first_for_each(cb)
    

  """
  Stretch goal
  
  The breadth first search is best implemented using Queue data structure, so I implemented the Queue method in another file and then use it here. In addition, I implemented the Linked List method because Queue uses Linked List in its code.
  Here, we're going to add to the queue, then use a loop to check the situation.
  We're going to store the dequeued item in current_node and check if it's empty or not. If it's empty then it means the queue is empty. If it's not empty, then we're going to hold the its value in a closure (lambda) so it can be used in the test file.
  Then we check if the current_node has any children; if it does, then we add them to the queue.
  """
  def breadth_first_for_each(self, cb):  # O(n)
    
    queue = Queue()	# O(1)
    
    queue.enqueue(self)	# adding self, root	# O(1)
  
    while True: # O(n)
 
      current_node = queue.dequeue()	# O(1)
      
      if current_node is None:
        return
   
      cb(current_node.value)	# O(1)
      
      if current_node.left is not None:
        queue.enqueue(current_node.left)	# O(1)
      if current_node.right is not None:
        queue.enqueue(current_node.right)	# O(1)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
