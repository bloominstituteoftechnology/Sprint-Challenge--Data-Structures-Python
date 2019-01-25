import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

namestwo = set(names_2)
duplicates = [a for a in names_1 if a in namestwo] #0(n) + 0(1) = 0(n)
# for name_1 in names_1:   #0(n)
#     for name_2 in names_2: #(n)
#         if name_1 == name_2:
#             duplicates.append(name_1) #0(1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

