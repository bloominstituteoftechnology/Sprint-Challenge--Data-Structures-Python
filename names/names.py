import time
import sys
sys.path.append('../ring_buffer')
from ring_buffer import DoublyLinkedList

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert value into tree
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if tree contains value, else False
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else: # Target is >= self.value
            # go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # call this function on the value of each node
    # recursive or iterative approach okay
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def dft_print(self, node):
        storage = Stack()
        current = self
        storage.push(current)
        while storage.len() > 0:
            current = storage.pop()  # call the pop fn
            print(current.value)
            if current.left:
                storage.push(current.left)
            if current.right:
                storage.push(current.right)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
#print (f"runtime: {end_time - start_time} seconds")


# LRU cache? Not textbuffer?




