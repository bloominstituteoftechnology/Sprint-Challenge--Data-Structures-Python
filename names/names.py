import time

start_time = time.time()

# Time complexity
# O(2n) where n is total number of names in names_1 and names_2

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names - O(n/2)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names - O(n/2)
f.close()

first = set(names_1)  # O(n/2) to copy the list to a set
second = set(names_2)  # O(n/2)

duplicates = first.intersection(second)  # O(min(len(first), len(second))) = O(n/2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# First output
    # runtime: 10.559283018112183 seconds

# Without nested for loops:
    # runtime: 0.005473136901855469 seconds
