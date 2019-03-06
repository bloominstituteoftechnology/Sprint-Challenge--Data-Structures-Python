import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#found built-in list and set modules for python, while researching duplicates strategies 
#underlying datastructure is hashing

duplicates = list(set(names_1) & set(names_2))
    
'''
#check all the names in names1
#check all the names in names2
#if any name matches in names1 and names2, add to duplicate array

for name_1 in names_1: O(n)
    for name_2 in names_2:O(n)
        if name_1 == name_2: O(n)
            duplicates.append(name_1)O(n)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

