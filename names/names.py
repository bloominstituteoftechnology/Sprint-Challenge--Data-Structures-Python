import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# create a dictionary of name_1 to compare against
name_1_dictionary = {}

# duplicates array to aggregate matches
duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:
    name_1_dictionary[name_1] = True

# if name_2 is found in name_1 dictionary using get() method, add it to duplicates
for name_2 in names_2:
    if name_1_dictionary.get(name_2, None):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

