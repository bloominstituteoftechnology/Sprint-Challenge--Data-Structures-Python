import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

name_list = []
name_list2 = []

for name in names_1:
    name_list.append(name)

for name in names_2:
    name_list2.append(name)

a = set(name_list)
b = set(name_list2)

c = a.intersection(b)

duplicates = c

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
