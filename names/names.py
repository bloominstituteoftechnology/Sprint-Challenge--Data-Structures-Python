import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Try 1: This is 2.1961 seconds in my laptop
# ****My Code Below Here ***
# names_list = names_1+names_2
# for name in names_list:     
#     if name not in duplicates:
#         duplicates.append(name)
# Try 2:         
# My Code below here - This is time is down to 1.264 seconds
# duplicates = [i for i  in names_1 if i in names_2 ]

#Try 3:
# My code below here: -- This one is under 0.006 seconds.
# name_dictionary = {}
# for name_1 in names_1:
#     name_dictionary[name_1] = True
# for name_2 in names_2:
#     if name_2 in name_dictionary:
#         duplicates.append(name_2)    




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

