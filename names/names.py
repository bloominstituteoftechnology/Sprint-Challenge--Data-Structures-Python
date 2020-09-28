import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode("Mike")
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if name_2 not in duplicates:
        if bst.contains(name_2):
            duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

########## SPEED TIMES ##########
########## BEFORE runtime: 6.172563314437866 seconds ##########
########## AFTER  runtime: 0.1124579906463623 seconds ##########
########## SHAVED NEARLY 6 SECONDS OFF TIME ##########

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
