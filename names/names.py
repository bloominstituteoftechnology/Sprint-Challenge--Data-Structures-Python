import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#pulls names from list 1, then list 2, compares them and then adds duplicates
#duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
#runtime: 7.993720531463623 seconds

#compares names in list 2 to list 1 as it pulls them and adds duplicates
duplicates = []
setName = set(names_1) #builds collection of names in list 1 to compare before comparing
for name in names_2:
    if name in setName:
        duplicates.append(name)
#first runtime: 1.406482219696045 seconds
#second runtime: 0.009005546569824219 seconds


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

