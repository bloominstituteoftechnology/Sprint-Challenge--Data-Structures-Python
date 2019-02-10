import time

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
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# trying to implement a binary search class to help with duplicate searching

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.duplicates = []

    def insert(self, value):
        new = BST(value)
        if (value < self.value):
            if not self.left:
                self.left = new
            else:
                self.left.insert(value)
        elif (value >= self.value):
            if not self.right:
                self.right = new
            else:
                self.right.insert(value)