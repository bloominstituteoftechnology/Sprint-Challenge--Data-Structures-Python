import time
from bst import BSTNode

start_time = time.time()

f = open('/Users/Prapti/Lambda School/Sprint Challenges/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/Users/Prapti/Lambda School/Sprint Challenges/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime: 0.20615649223327637 seconds which is under 0.6 seconds

bst = BSTNode("None")
duplicates = []

for name in names_1:
    bst.insertValue(name)
for name in names_2:
     if bst.containsTarget(name):
         duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n{', '.join(duplicates)}\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

