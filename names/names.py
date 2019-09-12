import time

start_time = time.time()

f = open('names_1.txt', 'r') 
names_1 = f.read().split("\n")  # List containing 10000 names    
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names  
f.close()

# duplicates = []
# for name_1 in names_1: 
#     for name_2 in names_2: 
#         if name_1 == name_2:
#             duplicates.append(name_1)     O(n^2)
list1 = names_1
list2 = names_2
#did this in JS at work last tuesday (a lil diffrent but still works)
duplicates = set(list1) & set(list2)  # O(2n) = O(n)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

