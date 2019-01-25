import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

non_duplicates = {}
duplicates = []

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# I'm imagining that they are expecting me to use binary search. 
# But I think that a hash table is more efficient.

for name in names_1:
    non_duplicates[name] = 1

for name in names_2:
    try:
        non_duplicates[name] += 1
    except: 
        pass

for name in non_duplicates:
    if non_duplicates[name] > 1:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Less than one hundredth of a second. Total time is O(n)