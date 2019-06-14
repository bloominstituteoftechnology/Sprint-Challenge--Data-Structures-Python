import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

t = BinarySearchTree()

duplicates = []
for name_1 in names_1:
    t.insert(name_1)

for name_2 in names_2:
    if t.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


def search(lst, target):
    if lst is None:
        return None
    min = 0
    max = len(lst)-1
    if max == -1:
        return None
    elif max == 0:
        return max if lst[0] == target else None
    avg = (min+max) // 2
    # uncomment next line for traces
    # print (lst, target, avg)
    while (min < max):
        if (lst[avg] == target):
            return avg
        elif (lst[avg] < target):
            s = search(lst[avg+1:], target)
            if s is None:
                return None
            return avg + 1 + search(lst[avg+1:], target)
        else:
            s = search(lst[:avg], target)
            if s is None:
                return None
            return s

    # avg may be a partial offset so no need to print it here
    # print "The location of the number in the array is", avg
    return avg

names_1.sort()
s1 = names_1
# print('Ah search', search(s1, "Ahmad Watts"))

start_time = time.time()
duplicates = []

for name_2 in names_2:
    if search(s1, name_2) is not None:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates list only:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime list only: {end_time - start_time} seconds")

# for list only runtime complexity is O(n log n), space complexity is O(n)
