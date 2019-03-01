from collections import Counter
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# names_first = Counter(names_1)
# names_second = Counter(names_2)
# for key in names_first:
#     if key in names_second:
#         duplicates.append(key) - fastest solution

for name in names_1:
  if name in names_2:
    duplicates.append(name) # slower stretch solution using only arrays

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

