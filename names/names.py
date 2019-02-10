import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# maybe a hash table would be a better solution since these are simple comparisons

duplicates = []
single_names = {} # since sets use hash tables, we can do index matching quickly regardless of the number of entries

for name in names_1: 
    single_names[name] = 1 # add names from the first name list to single_names set

for name in names_2:
    try:
        single_names[name] += 1 # add the names from the second name list as well
    except: # until all the names have been added
        pass

for name in single_names: 
    if single_names[name] > 1:
        duplicates.append(name) # check the set to see multiple appearances of the same name and append to duplicates list

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

###### OLDER CODE ######
# trying to implement a binary search class to help with duplicate searching
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.duplicates = []

#     def insert(self, value):
#         new = BST(value) # set up a new value to store certain nodes
#         if self.value == value:
#             duplicates.append(value)
#         if (value < self.value): # comparing each value, moving it to the left if it is the smaller value
#             if not self.left:
#                 self.left = new
#             else:
#                 self.left.insert(value)
#         elif (value >= self.value): # if the value is larger, move it to the right
#             if not self.right:
#                 self.right = new
#             else:
#                 self.right.insert(value)
    
#     def contains(self, target):
#         # checks to see if value is equal to target, uses this recurisvely for left and right trees as well
#         if self.value == target:
#             return True
#         if self.left:
#             if self.left.contains(target):
#                 return True
#         if self.right:
#             if self.right.contains(target):
#                 return True
#         return False

# # testing and returns

# duplicates = []

# first = names_1.pop(0)

# binarySearch = BST(first)
# for name in names_1:
#     binarySearch.insert(name)
# for name in names_2:
#     if binarySearch.contains(name):
#         duplicates.append(name)

# print(binarySearch)
# print(binarySearch.duplicates)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

###### END OLDER CODE ######