import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = [] # O(n) space complexity
# O(n**2) time complexity
# for name_1 in names_1:  # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: # O(1)
#             duplicates.append(name_1) # O(1)

# I beleive the following is still a O(n^2) runtime solution. But the time went from 6 seconds to 1 second.
duplicates = [name for name in names_1 if name in names_2]


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

