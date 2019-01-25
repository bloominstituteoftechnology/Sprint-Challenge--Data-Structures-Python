import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [] 
set_names = set()
set_names.add(tuple(names_1))
for name in names_2:
    if name in set_names:
        duplicates.append(name)
    

# I beleive the following is still a O(n^2) runtime solution. But the time went from 6 seconds to 1 second.
# duplicates = [name for name in names_1 if name in names_2]



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

