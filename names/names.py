import time
from collections import defaultdict

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
duplicates = []
d = defaultdict(int)
for name in names_1:
    d[name] += 1
for name in names_2:
    if d[name]:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Original runtime: 10.29637098312378 seconds
# My runtime: 0.01481175422668457 seconds