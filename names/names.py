import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
names = {}
for i in names_1:
    names[i] = i
for i in names_2:
    if i in names:
        duplicates.append(names[i])
        
#duplicates = []
# for name_1 in names_1:               
#     for name_2 in names_2:            
#         if name_1 == name_2:         
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
