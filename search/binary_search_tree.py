import time
from queue import *

start_time = time.time()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    # left_tree = BinarySearchTree(self.left)
    # # left_mega_tree = BinarySearchTree(self.left.left)
    # right_tree = BinarySearchTree(self.right)
    # # right_mega_tree = BinarySearchTree(self.right.right)
    # if self.value is None:
    #     return cb(None)
    # if not self.left:
    #   return cb(self.value)
    #   print("What", self.value)
    # if self.value:
    #   cb(self.value)
    #   print("4??",self.value)
    # if self.left:
    #     cb(self.left.value)
    #     # self.left = left_tree
    #     print("4??",self.left.value)
    # if self.right:
    #     cb(self.right.value)
        
    #     print("is it 4:::", self.right.value)
    # if self.left.left:
    #     print("is it 4###", self.value)
    #     # cb(self.left.right.value)
    # if self.left.right:
    #     print("is it 4!?!?!", self.left.right.value)
    #     # self.right = right_tree
    #     # self.left = left_tree
    #     cb(self.left.right.value)
    #     print(self.right)
    # self.left = left_tree
    # # print("test: ", self.left.value)
    # # print("test: ", self.left)
    # cb(self.right.left.value)
    # cb(self.right.right.value)
    # # print("test1: ", self.left.left.value)

    q = []
 

    q.append(self)
    while len(q) > 0:
      que = q.pop(0)
      # visited.append(que)
      if que.left:
        q.append(que.left)
      if que.right:
        q.append(que.right)
      cb(que.value)
    

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
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

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



end_time = time.time()

print (f"runtime: {end_time - start_time} seconds")