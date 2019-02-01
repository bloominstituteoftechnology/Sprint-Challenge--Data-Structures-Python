import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:  #O(n)
#     for name_2 in names_2:   #O(n)
#         if name_1 == name_2:   
#             duplicates.append(name_1)  #O(1)

set_names_1 = set(names_1) 
set_names_2 = set(names_2)
set_names = set_names_1|set_names_2 #make union between sets
duplicate_names = set_names_1 & set_names_2 #intersetion prints out only repeated names
duplicates = list(duplicate_names)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

