import time

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
end_time = time.time()
print (f"\n{len(duplicates)} duplicates:\n{', '.join(duplicates)}\n")
print (f"Two for-loops runtime: {end_time - start_time} seconds\n\n")
# Two for-loops runtime: 5.52326512336731 seconds

start_time = time.time()
duplicates = []
names_3 = names_2
names_3.sort()
length = len(names_2)
for name_1 in names_1:
    i, j = 0, length-1
    while True:
        k = i + int((j-i)/2)
        name_2 = names_3[k]
        if name_1 < name_2:
            j = k
        elif name_1 > name_2:
            i = k
        else:
            duplicates.append(name_2)
            break
        if i+1 >= j:
            name_2 = names_3[j]
            if name_1 == name_2:
                duplicates.append(name_2)
            break
end_time = time.time()
print (f"{len(duplicates)} duplicates")
print (f"Binary search runtime: {end_time - start_time} seconds\n")
# Binary search runtime: 0.08876609802246094 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time = time.time()
# duplicates = []
# for n in names_1:
#     if n in names_2:
#         duplicates.append(n)
duplicates = [n for n in names_1 if n in names_2]
end_time = time.time()
print (f"{len(duplicates)} duplicates")
print (f"Built-in method runtime: {end_time - start_time} seconds\n")
# Built-in method runtime: 0.8597457408905029 seconds

# ---------- Other Methods -----------
start_time = time.time()
l = list(set(names_1)) + list(set(names_2))
duplicates = [l[i] for i in range(len(l)) if l[i] in l[:i]]
end_time = time.time()
print (f"{len(duplicates)} duplicates")
print (f"Alternative method runtime: {end_time - start_time} seconds\n")
# Alternative method runtime: 2.8357491493225098 seconds