import time
from doubly_linked_list import DoublyLinkedList

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
name_list = DoublyLinkedList()
for name_1 in names_1:
    name_list.add_to_tail(name_1)

for name_2 in names_2:
    if name_list.contains(name_2):
        duplicates.append(name_2)

# def search(arr, target):
#     middle_idx = int(len(arr) / 2)
#     idx = 0
#     while idx < middle_idx:
#         if arr[idx] == target:
#             return True
#         idx += 1
#     while middle_idx < len(arr):
#         if arr[middle_idx] == target:
#             return True
#         middle_idx += 1
#     return False

# for name_2 in names_2:
#     if search(names_1, name_2):
#         duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
