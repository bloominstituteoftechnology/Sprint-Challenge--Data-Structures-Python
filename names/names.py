import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

l_names1 = []  # Return the list of duplicates in this data structure
l_names2 = []
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:
    l_names1.append(name_1)
for name_2 in names_2:
    l_names2.append(name_2)

set_1 = set(l_names1)
set_2 = set(l_names2)

duplicates = list(set_1.intersection(set_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n")
print(f"{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
