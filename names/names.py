import time
import os

file_names_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'names_1.txt')
file_names_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'names_2.txt')

start_time = time.time()

f = open(file_names_1, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(file_names_2, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
