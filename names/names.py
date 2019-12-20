import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [] # Runtime is  above 1 sec/ 1.63 s
for names_2 in names_2:
    if names_2 in names_1:  #  two loops, but fair time complexity 
        duplicates.append(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
# Method used  below (Deploys a set, which was restricted) results in a runtime > 0.01s 
cache = {}
for names_1 in names_1:
    cache[names_1] = names_1
for names_2 in names_2:
    if names_2 in cache: # Python method built-in set allocates improved runtime complexity
        duplicates.append(names_2)