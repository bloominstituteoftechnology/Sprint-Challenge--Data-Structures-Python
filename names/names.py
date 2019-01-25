import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# As nested for loops Time complexity is O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


name_from_first = {}
for name_1 in names_1:
    name_from_first[name_1] = name_1

#print(name_from_first)

#duplicates = [name_2 for name_2 in names_2 if names_2 in name_from_first.keys()]
duplicates = []
for name_2 in names_2:
    if name_2 in name_from_first:
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
#Runtime reduced to `runtime: 0.007979154586791992 seconds` by using dict -- key:value data structure 
# Two for loops but not nested so time complexity is O(n) 
