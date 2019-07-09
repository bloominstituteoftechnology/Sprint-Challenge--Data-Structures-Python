import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#BEGIN NEW LOG
duplicates = [] 
namesList = names_1 + names_2
namesList.sort()
nameLen = len(namesList)-2
for i in range(nameLen):
    if namesList[i] == namesList[i-1]:
        duplicates.append(namesList[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

