import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# run time average around 13 seconds after about 5 runs.
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# run time is now 0.012 secs if using set BUT since we're not allowed to use set in this case.
# names_1 = set(names_1)
# duplicates = [x for x in names_2 if x in names_1]

# run time is now average around 0.015 secs
duplicates = []
names_dictionary = {}

for name in names_1:
    names_dictionary[name] = 'original'

for name in names_2:
    if name in names_dictionary:
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
