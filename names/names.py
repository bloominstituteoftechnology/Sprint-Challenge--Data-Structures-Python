import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
#intersection to find duplicates
name_set = set(names_1).intersection(set(names_2))
duplicates=[]
for i in name_set:
#finds the smaller of the two lists
    num = (min(names_1.count(i), names_2.count(i)))
    for j in range(num):
        duplicates.append(i)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

