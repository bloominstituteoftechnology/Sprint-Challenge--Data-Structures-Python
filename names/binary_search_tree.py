class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    if value < self.value:
        if not self.left:
            self.left = node
        else:
            self.left.insert(value)
    # if value is less than self.value
    ## check if left is none
    ## if so, set left to be this node
    ## if not None, call the left node's insert with this value
    if value >= self.value:
        if not self.right:
            self.right = node
        else:
            self.right.insert(value)

    ## if value is greater than self.value
    #check if right is none
    # if it is none, set right to be a node
    # if it has a node, call self.right.insert with this value
  def contains(self, target):
    ## if self.value is target,
    ## return true
    ## if target is less than self.value,
    ## check if we have a left
    ## if so return left.contains on the targetself.
    ## if not, return false
    # if self.value == target:
    #     return True
    # elif self.right is None and self.left:
    #     return False
    # else:
    #     if self.left:
    #         if self.left.contains(target):
    #             return True
    #
    #     if self.right:
    #         if self.right.contains(target):
    #             return True
    if self.value == target:
        return True
    if self.value > target and self.left:
        if self.left.contains(target):
            return True
    elif self.value < target and self.right:
        if self.right.contains(target):
            return True
    else:
        return False
     ## otherwise, the target must be greater than self.value
     ## check if we have a right
     ## if so, reutrn self.right.contains on the targetself
     ## if not, return False

  def get_max(self):
    if self.right is None:
        return self.value
    else:
        return self.right.get_max()
     # if we have a right
     # return right's get max
     # otherwise, return self.value

  def for_each(self, cb):
    cb(self.value)
    if self.right:
        self.right.for_each(cb)
    if self.left:
        self.left.for_each(cb)
    # call the callback on the self's value
    # cb(self.value)
    # if self.right
    # call rightie's for_each with cb
    #
    # if self.left
    # call lefti's for_each with cb
