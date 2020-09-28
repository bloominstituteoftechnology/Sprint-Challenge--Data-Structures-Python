import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:  # original code was loop within a loop which is Quadratic O(2^n)
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode('M')  # time complexiciy is Logarithmic O(log n)
for name1 in names_1:
    bst.insert(name1)
for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

'''
starter code took: 
runtime: 7.136850118637085 seconds
Mohds-MacBook-Air:names mohdraza$ 
'''
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# duplicates = [name1 for name1 in names_1 for name2 in names_2 if name1==name2] # runtime: 3.849382162094116 seconds
# duplicates = list(set(names_1) & set(names_2)) # runtime: 0.004938840866088867 seconds
duplicates = list(set(names_1).intersection(names_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
