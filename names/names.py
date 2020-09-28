import time
from name_tree import NameNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# -------- OLD TIME COMPLEXITY: O(n^3) ------------
# O(n) time complexity
# for name_1 in names_1:
      # O(n) time complexity
#     for name_2 in names_2:
          # O(n) time complexity
#         if name_1 == name_2:
#             duplicates.append(name_1)
# O(n) * O(n) * O(n) ---> O(n^3) 
# Average time: 5.8 seconds


# -------- NEW TIME COMPLEXITY: O(n) ----------
root = NameNode(names_1[0])

# O(n) time complexity
for index in range(1, (len(names_1) - 1), 1):
    root.insert(names_1[index])

# O(n) time complexity
for name in names_2:
    # O(log n) time complexity
    if root.contains(name):
        duplicates.append(name)
# O(n) + O(n) + O(log n) ---> O(2n) + O(log n) ---> O(2n) ---> O(n)
# Average time: 0.13 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n{', '.join(duplicates)}\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
