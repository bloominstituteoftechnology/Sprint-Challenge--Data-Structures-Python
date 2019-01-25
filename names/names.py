import time


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
name_1_dict = {}
name_2_dict = {}
for name_1 in names_1:
    name_1_dict[name_1.lower().replace(" ", "")] = name_1


for name_2 in names_2:
    name_2_dict[name_2.lower().replace(" ", "")] = name_2


for key in name_1_dict.keys():
    if name_2_dict.get(key):
        duplicates.append(name_1_dict.get(key))
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
