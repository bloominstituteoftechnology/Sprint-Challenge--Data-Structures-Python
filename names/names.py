import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

## Original double for loop garbage

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

## Solution using sets

name1 = set(names_1)
name2 = set(names_2)
duplicatesB = name1 & name2

## Verifying both lists have the same names. Length of same list should return 64

# verify = set(duplicates)
# sameList = verify & duplicatesB

#print(len(sameList))



end_time = time.time()
print (f"{len(duplicatesB)} duplicates:\n\n{', '.join(duplicatesB)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

