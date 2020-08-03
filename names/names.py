import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Polynomial Runtime - O(n^2)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Linear Time O(n) - Runtime less than 2 seconds
for name in names_1:
    if name in names_2:
        duplicates.append(name)

# List Comprehension - Runtime less than 2 seconds
# duplicates = [name for name in names_1 if name in names_2]

# Set Functions to list - Runtime less than 1 second
# duplicates = list(set(names_1) & set(names_2))

# set().intersection() - Runtime less than 1 second
# duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
