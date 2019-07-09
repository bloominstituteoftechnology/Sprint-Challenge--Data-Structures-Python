import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

