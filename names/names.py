import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

#for name_1 in names_1:        # O(n^2)
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
            
"""
Having a loop inside a loop (above) is not very good for big O.
The best way is to bring the second loop out, and use a set() to store the names then check the set() to see if it contains the name_item that we're looking for.
If it does, then we add the name to duplicates_array.
"""            

name_lookup = set()		# O(1)

for name_1 in names_1:	# O(n)
    name_lookup.add(name_1)	# O(1)

for name_2 in names_2:	# O(n)
    if name_2 in name_lookup:	# O(1)
        duplicates.append(name_2)	# O(1)

# Total runtime complexity: O(2n) => O(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

