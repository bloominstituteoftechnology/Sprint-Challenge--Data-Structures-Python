import time
start_time = time.time()

# names_1 = BinarySearchTree('M')
# names_2 = BinarySearchTree('M')


names_dict = {}

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # O(n) operation to store names in dictionary ,  List containing 10000 names
for name in names_1:
    names_dict[name] = name
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # O(n) operation to store names in list List containing 10000 names
f.close()

duplicates = []
for name in names_2:       #O(n) operation to loop through all names in list
    if name in names_dict:   #O(1) operation to check if exists in dict
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

