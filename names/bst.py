class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check if the new nodes value < current value
        # if its then check if they have a child
        if value <= self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
      # contains works the same as insert although we are just searching the value
       # We need to check if the current target is the same as the self.value target.
        if target is self.value:
            return True
        if target < self.value:
            if not self.left:
                return self.left
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return self.right
            else:
                return self.right.contains(target)

    def get_max(self):
      # Get the current value and set it as max value
        cur_max = self.value
        # we know that the right side will always be largest
        if not self.right:
          # if its not just return the current max value
            return cur_max
          # if the right side is largest lets keep checking if it has a child and if its has a larger number.
          # if its not return the right largest number
        return self.right.get_max()

    def for_each(self, cb):
        # wrap the value in the cb
        cb(self.value)
        if self.left:
          # if left is true for each run the cb function
            self.left.for_each(cb)
        if self.right:
          # uf the right is true for each run the cb function  recusively
            self.right.for_each(cb)
