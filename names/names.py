import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")"""


# Written response:
#
# took about 8.24 seconds on my laptop.
# this approach uses a double for-loop, so it's runtime will be quadratic. 
# without knowing precisely how the '==' operator is implemented,
# it's difficult to be more specific, but it's runtime is likely
# proportional to the length of the shortest string in the expression.
# appending to the array also has a constant runtime.
# in this case we could probably assume the time complexity of the two to be some 
# constant, S. The runtime is then O(S(n^2)), and by convention
# the constant is dropped, leaving us with O(n^2).


# Approach with data structures from this week:

# python's comparison operators work by default with strings, no assembly required.
# so our existing binary search tree class should work just fine!

from binary_search_tree import BSTNode

# list of dupes
dupes = []

# instantiate the bst on the first name in the first list
the_lorax = BSTNode(names_1[0])

# insert the rest, skip the first.
[the_lorax.insert(name) for name in names_1[1:]]


for name in names_2: # Iterate over the second list (O(n))
    if the_lorax.contains(name): # check for the name's presence (O(log(n)))
        dupes.append(name) # add it to our list (O(constant))

end_time = time.time()
print (f"{len(dupes)} dupes:\n\n{', '.join(dupes)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# this approach finished in 0.13 seconds on my machine.
# it should have a time complexity of O(n*log(n)).


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Taking a swing at the other stretch mentioned in the README as well - 
# assuming I am only allowed to use python lists due to memory constraints.

start = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# sort names_1 and names_2
names_1 = sorted(names_1)
names_2 = sorted(names_2)

# now that the names are sorted, we can bolster our loop with a kind of 
# radix sort technique. we know two names can't be dupes if their 
# first letters don't match, and we know they're in alphabetical order.
# so the outer loop will hit every name in the first list,
# and the inner loop will hit every name in the second, but break
# as soon as the second loop hits names with first letters later
# than the first letter of the name the outer loop is on.

# we can extend this further by breaking the first sorted list into two 
# separate lists, the latter of which we'll reverse. we use the same approach,
# but for the top half we run in ascending order and the bottom in descending order.
# if the names are evenly distributed by their first letters, we should then
# end up only ever having to search through half the list to either match or break.

# this approach is nowhere near the speed of binary trees, but it runs in 6.73
# seconds compared to the original 8.24. additional approaches might entail
# breaking each of the two lists into 26 lists, one for each first letter, and 
# assigning to those lists at load-in. then the same approach can be used on the 
# second letter of the names in each list.


names_1_top = names_1[:5000]
names_1_bottom = names_1[5000:]
names_1_bottom.reverse()

dupes = []

for name_1 in names_1_top:
    for name_2 in names_2:
        # if the first letter in name_2 > the first letter in name one, break the loop.
        if name_2[0] > name_1[0]:
            break
        if name_1 == name_2:
            dupes.append(name_1)

names_2.reverse()

for name_1 in names_1_bottom:
    for name_2 in names_2:
        # if the first letter in name_2 < the first letter in name one, break the loop.
        if name_2[0] < name_1[0]:
            break
        if name_1 == name_2:
            dupes.append(name_1)

print (f"{len(dupes)} dupes")
end = time.time()
print(end - start)