import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Create dictionary to check names against
check = {}
# create list to store duplicates
duplicates = []
# Loop through first list and add to check
for name_1 in names_1:
    check[name_1] = True

# Loop through second list and get name out of check dict
# If in check add to duplicates
for name_2 in names_2:
    if check.get(name_2, None):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
