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


def binary_search(name1, name2):
    index = 0
    index2 = 0
    # duplicates = []
    while index < len(name1):
        if name1[index] == name2[index2]:
            duplicates.append[name2[index2]]
            index2 += 1
            index += 1
        index += 1


print(binary_search(names_1, names_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
