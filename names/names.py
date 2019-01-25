import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# runtime: 7.971049785614014 seconds
# duplicates = []
# for name_1 in names_1:  # O(n)
#     for name_2 in names_2:  # O(n)
#         if name_1 == name_2:  # O(1)
#             duplicates.append(name_1)  # O(1)

# First pass
# runtime: 1.465162992477417 seconds
# duplicates = []
# for name_1 in names_1:  # O(n)
#     if name_1 in names_2:  # O(n) bec "in" operator is O(n) in lists
#         duplicates.append(name_1)  # O(1)

# Optimized
# runtime: 0.006497859954833984 seconds
duplicates = list(set(names_1) & set(names_2))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

