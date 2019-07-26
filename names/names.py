import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_all = names_1 + names_2

# Get counts
counts = {}

for i in names_all:
  try:
    counts[i] += 1
  except:
    counts[i] = 1

# Duplicates have counts > 1
duplicates = [k for k,v in counts.items() if v > 1]


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
