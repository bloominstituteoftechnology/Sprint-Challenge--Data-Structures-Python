import time
## ________ Provided Solution __________
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Provided Solution - Runtime O(n^n)
duplicates = []
for name_1 in names_1: # O(n)
    for name_2 in names_2: # O(n)
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print ("\n\nProvided Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

## ________ My solution section ____________
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# My Solution - Runtime O(5n) 
names1_set = set(names_1) # O(n) Use set() to remove duplicates within my lists. 
names2_set = set(names_2) # O(n)
count_table = {}
for name in names1_set: # O(n)
    count_table[name] = 1
for name in names2_set: # O(n)
    if name in count_table:
        count_table[name] += 1
    elif name not in count_table:
        count_table[name] = 1
duplicates = [k for (k,v) in count_table.items() if v > 1] # O(n)


end_time = time.time()
print ("\n\nMy Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
