import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# This solution is better than the solution above because 
# its not using any extra space, it's returning the duplicates names
# straight from the 2 original lists, in the above solution I created a third list
# to get the job done, in this one my space complexity is O(n).

print (f"stretch goal: {', '.join(set(names_1).intersection(names_2))}")