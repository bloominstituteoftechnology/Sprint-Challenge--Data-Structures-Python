import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

start_time = time.time()

duplicates2 = [x for x in names_1 if x in names_2]

end_time = time.time()
print (f"{len(duplicates2)} duplicates2:\n\n{', '.join(duplicates2)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
