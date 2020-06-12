import time

## original runtime complexity is O(n^c) and for frame of reference runs in 9.16 seconds on my computer
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Runtime complexity for this should be O(n) since iterating through a list is O(n).
# Reduced runtime on my computer to 2.15 seconds
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# Stretch: Runtime complexity for this is O(1) since dictionaries are a O(1) complexity for searching
# Reduced runtime on my computer to 0.011 seconds
names1_dict = {names_1[i] : i for i in range(0, len(names_1))}
names2_dict = {names_2[i] : i for i in range(0, len(names_2))}
for key in names1_dict:
    if key in names2_dict:
        duplicates.append(key)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
