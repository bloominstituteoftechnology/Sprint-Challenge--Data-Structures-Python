import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()



# Replace the nested for loops below with your improvements
set_names_1 = set(names_1)
set_names_2 = set(names_2)

duplicates = (set_names_1.intersection(set_names_2))

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

#Runtime of starter code: 7.9162 seconds
#Runtime of optimized code: 0.0048 seconds.

#The original starter code has a Time Complexity of at least O(n^2) due to iterating through the second list for every item in the first list.
#According to wiki.python.org/moin/TimeComplexity, each of the set() operations is O(n), and intersection is O(min(len(first_set), len(second_set))
#Therefore time complexity on this operation is O(n)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
