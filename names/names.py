"""
Task 2. Runtime Optimization

!Important! If you are running this using PowerShell by clicking on the green play button, 
you will get an error that names1.txt is not found. To resolve this, run it, get the error, 
then cd into the names directory in the python terminal that opens in VSCode.

Navigate into the names directory. Here you will find two text files containing 
10,000 names each, along with a program names.py that compares the two files and 
prints out duplicate name entries. Try running the code with python3 names.py. 
Be patient because it might take a while: approximately six seconds on my laptop. 
What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. 
Can you get the runtime to under a second? Under one hundredth of a second?

You may not use the built in Python list, set, or dictionary in your 
solution for this problem. However, you can and should use the provided duplicates 
list to return your solution.

(Hint: You might try importing a data structure you built during the week)
"""
from binary_search_tree import BSTNode # Import Binary Search Tree for use in this problem
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

list_duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
### complexity of the provided starter code is O(n^2)

# for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

# lets improve on that provided lists of names look-up code 
# Binary Search Tree for faster name look-up
BST = BSTNode(names_2[0]) # initialize BST with the first name in 'names_2'
for name in names_1[1:]: # begin by slicing 'names_01' list down the middle
    BST.insert(name) # insert this 1st slice into our BST

for name_2 in names_1: # search for dupliactes of names in 'names_1' in 'names_2'
    if BST.contains(name_2): # compare name values in BST ('names_1') to 'names_2' values
        list_duplicates.append(name_2) # add them to dupicates list

end_time = time.time()
# print (f"{len(list_duplicates)} duplicates:\n\n{', '.join(list_duplicates)}\n\n")
print (f"BST runtime: {end_time - start_time} seconds")
# now runtime complexity is O(n log n) since we are using BST 


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

"""
Say your code from names.py is to run on an embedded computer with very limited RAM. 
Because of this, memory is extremely constrained and you are only allowed to store 
names in arrays (i.e. Python lists). How would you go about optimizing the code under 
these conditions? Try it out and compare your solution to the original runtime. 
(If this solution is less efficient than your original solution, include both and label 
the strech solution with a comment)
"""

# I really can't think of a better solution in the allotted time although I'm sure there is one
# so I'm going to try using the .intersection() method

start_time = time.time()

for i in range(100):
    list_duplicates_1 = set(names_1).intersection(set(names_2)) # built-in python tool might be more efficient?

end_time = time.time()

print(f"Attempt at improved runtime: {(end_time - start_time)} seconds\n")
# NO - the python .intersection() method does NOT run faster than our code
# BST runtime: 0.06711864471435547 seconds
# "Improved" runtime: 0.10357379913330078 seconds