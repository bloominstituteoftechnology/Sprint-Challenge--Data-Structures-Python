import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
duplicates = []

# tuples take up less space and are faster to run than lists but aren't immutable gets 0.93621
# [names1, names2] = (names_1), (names_2)

# for name in names1:
#     if name in names2:
#         duplicates.append(name)

# using python set seems faster.. very weird gets 0.00499
setFirst = set(names_1)
for name in names_2:
    if name in setFirst:
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
