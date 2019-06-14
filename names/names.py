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

# duplicates = []
# name_dict = {}
# for name_1 in names_1:
#     name_dict[name_1] = True
# for name_2 in names_2:
#     if name_2 in name_dict:
#         duplicates.append(name_2)

duplicates = []
def binary_search(item, arr):
    l = 0
    h = len(arr)
    while True:
        m = (h + l) // 2
        if item == arr[m]:
            return True
        if h - l == 1:
            return False
        if arr[m] > item:
            h = m
        else:
            l = m

names_1 = sorted(names_1)
duplicates = [x for x in names_2 if binary_search(x, names_1)]


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(sorted(duplicates))}\n\n")
print (f"runtime: {end_time - start_time} seconds")

