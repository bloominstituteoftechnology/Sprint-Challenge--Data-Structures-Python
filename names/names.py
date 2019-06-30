import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Whatever we do we want to avoid this O(n^2) runtime...
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1) # runtime of ~5.8-6.5 seconds on my computer

# Compare with a list comprehension 
#names = [name for name in names_1 if name in names_2]
#for name in names: #O(n)
#    duplicates.append(name) runtime of ~1.27 seconds on my computer

# Essentially the same as the list comprehension but with less space complexity.
for name in names_1: # O(n)
    if name in names_2: 
        duplicates.append(name) # runtime of ~1.28 seconds on my computer

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

