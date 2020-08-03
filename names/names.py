import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# ------------ original inefficient code -------------------
""" The timing of this ^^^ code took approximately 7.87 seconds. """
#
# duplicates = []  # Return the list of duplicates in this data structure
#
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# -----------------------------------------------------------



# More efficient code in a single line
""" This code took approximately 0.005 seconds! """
duplicates = set(names_1) & set(names_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

""" The fastest I could find is implemented above and would work 
excellently with lists and other data structures. It only takes 
0.005 seconds, well under the goal of 6 seconds! 
""" 