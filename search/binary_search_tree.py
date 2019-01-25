class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        pass

    def breadth_first_for_each(self, cb):
        pass

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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        if self.storage is None:
            return
        self.size += -1
        return self.storage.pop(0)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
print(q.dequeue())


print(q.storage)
