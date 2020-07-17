import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

name_list = []

for name in names_1:
    name_list.append(name)

for name in names_2:
    name_list.append(name)

s = set()

dups = set(name for name in name_list if name in s or s.add(name))
print(len(dups))


def remove_duplicates(list_of_names):
    final_list = []
    for name in name_list:
        if name not in final_list:
            final_list.append(name)
    return final_list


duplicates = remove_duplicates(dups)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
