# I am going to attempt to reduce the runtime of the
# origional names.py and my binary-search solution
# by using a dictionary to achieve O(n) time complexity, 
# and compare the results.

########################################
# NESTED FOR LOOP SOLUTION             #
# Time complexity: O(n**2)             #
# Runtime: 6.037697076797485 seconds   #
########################################

########################################
# BINARY SEARCH SOLUTION               #
# Time complexity: O(n log n)          #
# Runtime: 0.10671377182006836 seconds #
########################################

########################################
# DICTIONARY LOOKUP SOLUTION           #
# Time complexity: O(n)                #
# Runtime: 0.00598454475402832 seconds #
########################################

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
names_1_dict = {}
for i in names_1:
    names_1_dict[i] = 1

for i in names_2:
    if i in names_1_dict:
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

