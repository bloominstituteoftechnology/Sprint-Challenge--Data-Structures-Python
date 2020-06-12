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

bst = BSTNode(names_1[0])
for name in names_1[1:]:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this
# problem. What's the best time you can accomplish?  Thare are no restrictions
# on techniques or data structures, but you may not import any additional
# libraries that you did not write yourself.

print("\n   ---STRETCH VERSION USING SETS---\n")


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = list(names_1 & names_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---- using only lists ----

print("\n   ---STRETCH VERSION USING ONLY LISTS---\n")


def merge_sort(arr: list, left=0, right=None):
    right = len(arr) - 1 if right is None else right

    if left >= right:  # already sorted; size <= 1
        return arr

    # merge-sort each half
    mid1 = (left + right) // 2
    mid2 = mid1 + 1
    arr = merge_sort(arr, left, mid1)
    arr = merge_sort(arr, mid2, right)

    # merge
    while mid2 <= right:
        if arr[left] > arr[mid2]:
            arr.insert(left, arr.pop(mid2))
            mid2 += 1
        elif left < mid2 - 1:
            left += 1
        else:
            mid2 += 1
    return arr


def find_sorted(arr, item) -> bool:
    length = len(arr)
    if length == 0:
        return False
    elif length == 1:
        return arr[0] == item

    midpoint = len(arr) // 2
    if arr[midpoint] == item:
        return True
    elif item < arr[midpoint]:
        return find_sorted(arr[:midpoint], item)
    else:
        return find_sorted(arr[midpoint+1:], item)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = merge_sort(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []

names_1_length = len(names_1)

for name in names_2:
    if find_sorted(names_1, name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
