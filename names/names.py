import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

print(names_1)
print(names_2)

duplicates = []
duplicates2 = []
if len(names_1) > len(names_2):
    for name_1 in names_1:
        if name_1 in names_2:
            duplicates.append(name_1)
else:
    for name_2 in names_2:
        if name_2 in names_1:
            duplicates.append(name_2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates2.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# duplicates.sort()
# duplicates2.sort()

# print(duplicates == duplicates2)
