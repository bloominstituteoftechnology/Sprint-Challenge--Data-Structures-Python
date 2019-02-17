import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# # O(n) * O(n) * O(1) * O(1) = O(n^2)
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: # O(1)
#             duplicates.append(name_1) # O(1)

duplicates = set(names_1).intersection(set(names_2))

'''
Instructor Pseudo Code:

    Binary Search Tree Approach # O(n log n):
        - put all the names from names_2 into a BST # O(n log n)
            - for each  name in name_1, check if that name is in the BST # O(n log n)
            - if so, add to duplicates
        * note: wastes space on pointers

    Hash Table Approach # O(n):
        - put all the names from names_2 into a set # O(n)
            - for each  name in name_1, check if that name is in the set # O(n)
            - if so, add to duplicates
        * note: wastes space on buckets

    Quicksort Approach # O(n log n):
        - sort names_2 array using quicksort # O(log n)
            - for each name in name_1, run binary search on name_2 
            - if so, add to duplicates
        * note: optimal space efficiency
'''


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

