import time
import sys
sys.path.append('../search')

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst = BinarySearchTree("")

set_1 = set(names_1)

for name in names_2: # O(n)
    if name in set_1: # O(1)
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Stretch:


duplicates_stretch = []

def quick_sort( arr ):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [item for item in arr[1:] if item < pivot]
        high = [item for item in arr[1:] if item > pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)

    return arr


i = 0
j = 0
sorted_1 = quick_sort(names_1)
sorted_2 = quick_sort(names_2)

while i < len(sorted_1) and j < len(sorted_2):
  if sorted_1[i] == sorted_2[j]:
    duplicates_stretch.append(sorted_1[i])
    i += 1
    j += 1
  elif sorted_1[i] < sorted_2[j]:
    i += 1
  else:
    j += 1

end_time_stretch = time.time()
print (f"{len(duplicates_stretch)} duplicates:\n\n{', '.join(duplicates_stretch)}\n\n")
print (f"runtime: {end_time_stretch - end_time} seconds")
