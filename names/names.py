import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# merge names to single list
names = names_1 + names_2 

duplicates = []
# counter dict to keep track of previously encountered names
counter = {}

for name in names:
    # if name isn't in dict, initialize key to value of 1
      if not name in counter:
          counter[name] = 1
    # if name _is_ in dict, increase value by 1
    # add name to duplicates array
      else:
          counter[name] += 1
          duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

