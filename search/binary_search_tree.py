from queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # root -> left branch -> right branch
        cb(self.value)

        if self.left:
            self.left.depth_first_for_each(cb)
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        queue = Queue()  # FIFO
        # add initial value to the queue
        queue.enqueue(self)

        while queue:
            # take out every first element in the queue
            node = queue.dequeue()
            # add that popped element to the list
            cb(node.value)

            # append each subtree to the queue
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            if queue.len() == 0:
                break

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if value < self.value:
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


bst = BinarySearchTree(5)
bst.insert(3)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(11)
arr = []
cb = lambda x: arr.append(x)
print(bst.breadth_first_for_each(cb))
print(arr)
