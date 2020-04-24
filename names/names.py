import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


  

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
 
 
     

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")


begin_time = time.time()
duplicates = []
names_3 = names_2
names_3.sort()
length = len(names_2)
for name_1 in names_1:
    x, j = 0, length-1
    while True:
        k = x + int((j-x)/2)
        name_2 = names_3[k]
        if name_1 < name_2:
            j = k
        else:
            duplicates.append(names_2)
            break
        if x+1 >= j:
            name_2 = names_3[j]
            if name_1 == name_2:
                duplicates.append(names_2)
            break

end_time = time.time()
print (f"{len(duplicates)} duplicates")
print(f"BST: {end_time - begin_time} seconds\n")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
