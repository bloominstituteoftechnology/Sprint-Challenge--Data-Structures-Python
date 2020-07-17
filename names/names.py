import time
start_time = time.time()

with open('names_1.txt', 'r') as file:
	names_1 = file.read().split("\n") 
file.close()
with open('names_2.txt', 'r') as file:
	names_2 = file.read().split("\n") 
file.close()

duplicates = []

# Stretch 0(1) (0.008 seconds) 
# Dictionaries are hashed, do no need to iterate over everything
dictionary1 = {names_1[index] : index for index in range(0,10000)}
dictionary2 = {names_2[index] : index for index in range(0,10000)}

for name_1 in dictionary1:
	if name_1 in dictionary2:
		duplicates.append(name_1)

''' Version 2 O(n) (1.35 seconds)
for name_1 in names_1:
	if name_1 in names_2:
		duplicates.append(name_1)
'''

''' Version 1 O(n^x) (5.64 seconds)
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
