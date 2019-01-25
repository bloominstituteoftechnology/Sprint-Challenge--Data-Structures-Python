from collections import deque
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb, stack=[], visited=[]):
    #Preorder (Root, Left, Right)
    # stack = []
    # visited = []

    if len(stack) == 0:
      if self not in visited:
        stack.append(self)

    if len(stack) > 0:
      #pop last item from stack
      node = stack.pop()
    
      #add to visited
      visited.append(node.value)
      
      cb(node.value)

      #add its children to the stack, check if left child has value
      # if it does, do recursive call on its left value
      if self.left:
        stack.append(self.left)
        self.left.depth_first_for_each(cb, stack, visited)
      # if it does not, do recursive call on its right child
      if self.right:
        stack.append(self.right)
        self.right.depth_first_for_each(cb, stack,visited)
    # print(stack)
    return visited

  def breadth_first_for_each(self, cb, queue=deque(), visited=[]):
    print(list(queue))
    if len(queue) == 0:
      if self not in visited:
        queue.appendleft(self)
    if len(queue) > 0:
      node = queue.pop()
      visited.append(node.value)
      cb(node.value)
      if self.left:
        queue.appendleft(self.left)
        self.left.depth_first_for_each(cb, queue, visited)
      if self.right:
        queue.appendleft(self.right)
        self.right.depth_first_for_each(cb, queue,visited)
    return visited

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        #print(f'{value} is less than {self.value}. inserting in left side of {self.value}')
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        #print(f'{value} is greater than {self.value}. inserting in right side of {self.value}')
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

bst = BinarySearchTree(5)
bst.insert(3)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(11)

arr = []
cb = lambda x: arr.append(x)

print(bst.breadth_first_for_each(cb))
