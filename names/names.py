import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


sorted_arr = sorted(names_1)


def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = int((low+high)/2)
        midpoint = arr[middle]
        if midpoint > target:
            high = middle-1
        elif midpoint < target:
            low = middle+1
        else:
            return midpoint
    return -1


for name_2 in names_2:
    if binary_search(sorted_arr, name_2) is not -1:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
