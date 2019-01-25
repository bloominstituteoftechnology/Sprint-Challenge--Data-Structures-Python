from queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # Callback on value
        cb(self.value)
        # Recursively go down left side
        if self.left:
            self.left.depth_first_for_each(cb)
        # Once down going left go back up tree and go down right side
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # create queue
        queue = Queue()
        # put first node in queue
        queue.put(self)

        # while queue is not empty
        while not queue.empty():
            # Retrieve and remove first item in queue
            node = queue.get()
            # Callback function on value
            cb(node.value)

            # add left node to queue
            if node.left:
                queue.put(node.left)
            # add right item to queue
            if node.right:
                queue.put(node.right)

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
