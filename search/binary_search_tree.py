class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    """
    call the anonymous function on each node in the tree 
    this will require a current node variable to reference cb(current.value) for nodes
    for depth-first search we'll traverse the left tree as long as possible
    if this is not possible, go to the previous node
    from previous node, go down the right path until no longer possible, then the left path
    when these paths are complete, go back to previous node again and repeat
    """

    stack = [] # BFS uses stack structures rather than queue
    current = self
    # might need previous node variable, will test without one

    while True:
      cb(current.value)

      if current.right is not None: # add right trees to the stack where applicable
        stack.append(current)
      if current.left is None: # if no more left trees exist and the stack is clear, we are done
        if len(stack) == 0:
          break
        current = stack.pop().right # otherwise, we pop the right value or set it to the left tree if left values exist
      else: current = current.left    

  def breadth_first_for_each(self, cb):
    """
    use a queue rather than a stack for BFS
    enqueue the initial value
    once again we'll call the function on every node and check left/right, use dequeue to maintain FIFO ordering
    if there are no nodes in either direction, that level is complete and we can return
    for left and right values that are found, we enqueue those values next
    we can call this method recursively for further left/right nodes
    """

    x = Queue()
    x.enqueue(self.value)

    def bfs_recursive(current):
      cb(x.dequeue())
      if current.left is None and current.right is None:
        return # if no nodes on either side, the level is complete
      if current.left is not None:
        x.enqueue(current.left.value)
      if current.right is not None:
        x.enqueue(current.right.value) # for left and right values, enqueue those that are found
        
      # handle left/right nodes recursively
      if current.left is not None:
        bfs_recursive(current.left)
      if current.right is not None:
        bfs_recursive(current.right) # call the method on the nodes (not the values at those nodes)
      
    bfs_recursive(self)


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

# creating a Queue class for use with BFS solution

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, value):
    self.storage.append(value)
    self.size += 1

  def queue(self):
    if self.storage is None:
      return
    self.size -= 1
    return self.storage.pop(0)