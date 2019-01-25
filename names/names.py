import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

name_1_dict = {}
duplicates = []
for name_1 in names_1:
    name_1_dict[name_1] = True

for name_2 in names_2:
    if name_1_dict.get(name_2, None):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# First output
    # runtime: 10.559283018112183 seconds

# Without nested for loops:
    # runtime: 0.008630990982055664 seconds
