import time
from numba import jit
from binary_search_tree import BinarySearchTree
from hash_map import HashMap
import sys
from bisect import insort_right
from bisect import bisect_left 

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

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
        # t.delete(name_2)
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

    # print("The location of the number in the array is", avg)
    return avg


# print('Ah search', search(s1, "Ahmad Watts"))

start_time = time.time()
names_1.sort()
s1 = names_1
duplicates = []

for name_2 in names_2:
    if search(s1, name_2) is not None:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates list only:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime list only: {end_time - start_time} seconds")

# for list only runtime complexity is O(n log n), space complexity is O(n)

duplicates = []

def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # mi = 0
    while len(arrA) and len(arrB):
        while len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] <= arrB[0]:
                # merged_arr[mi] = arrA[0]
                # mi += 1
                if arrA[0] == arrB[0]:
                    duplicates.append(arrA[0])
                arrA = arrA[1:]
  
            else:
                break

        while len(arrB) > 0 and len(arrA) > 0:
            if arrB[0] <= arrA[0]:
                # merged_arr[mi] = arrB[0]
                # mi += 1
                if arrA[0] == arrB[0]:
                    duplicates.append(arrA[0])
                arrB = arrB[1:]
            else:
                break
        # if len(arrA) == 0 and len(arrB) > 0:
        #     for i in range(mi, len(merged_arr)):
        #         merged_arr[i] = arrB[0]
        #         arrB = arrB[1:]
        # elif len(arrA) > 0 and len(arrB) == 0:
        #     for i in range(mi, len(merged_arr)):
        #         merged_arr[i] = arrA[0]
        #         arrA = arrA[1:]

    # return merged_arr
start_time = time.time()
names_1.sort()
names_2.sort()
merge(names_1, names_2)
end_time = time.time()
print(f"{len(duplicates)} duplicates list only merge:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime list only merge: {end_time - start_time} seconds")

start_time = time.time()
duplicates = set(names_1) & set(names_2)
end_time = time.time()
print(f"{len(duplicates)} duplicates using set:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime using set: {end_time - start_time} seconds")

duplicates = []
c = compile("duplicates = set(_names_1) & set(_names_2)", "<char **>", "exec")
start_time = time.time()
_names_1 = names_1
_names_2 = names_2
exec(c)
end_time = time.time()
print(f"{len(duplicates)} duplicates using exec set:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime using exec set: {end_time - start_time} seconds")
duplicates_ = duplicates

@jit
def run_set():
    start_time = time.time()
    duplicates = set(names_1) & set(names_2)
    end_time = time.time()

print(f"{len(duplicates)} duplicates using jit set:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime using jit set: {end_time - start_time} seconds")    
run_set()

@jit
def run_hash():
    start_time = time.time()
    max_cells = 1000000
    cells = (max_cells // len(names_1)) * len(names_1)

    h = HashMap(cells)
    for n in names_1:
        h.add(n)
    def get_with_delete(n):
        r = h.get(n)
        if r:
            h.delete(n)
        return r    
    duplicates = [n for n in names_2 if h.get(n)]
    end_time = time.time()
    return end_time - start_time



rt = run_hash()
print(f"{len(duplicates)} duplicates using HashMap:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime using hash: {rt} seconds")   
if len(duplicates_ - set(duplicates)) > 0: 
    print('missing:', duplicates_ - set(duplicates))

@jit
def insort_right_sort(arr):
    r = []
    for i in arr:
        insort_right(r, i)
    return r    


@jit  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1  

duplicates = []

@jit
def bsearch():
    start_time = time.time()
    s1 = insort_right_sort(names_1) 
    for s in names_2:
        if BinarySearch(s1, s) >= 0:
            duplicates.append(s)      
    end_time = time.time()
    return end_time - start_time   

rt = bsearch()
print(f"{len(duplicates)} duplicates using bisec:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime using bisec: {rt} seconds")  


