import time

start_time = time.time()

with open('names_1.txt', 'r') as names1:
    with open('names_2.txt', 'r') as names2:
        duplicates = set(names1).intersection(names2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}")
print (f"runtime: {end_time - start_time} seconds")