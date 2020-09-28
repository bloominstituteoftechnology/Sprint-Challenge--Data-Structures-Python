import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode(names_1[0])

# adding first name file to the tree
for name in names_1:
    # using insert function
    bst.insert(name)

# checking for duplicates
for name in names_2:
    # using contain function to find duplicates
    if bst.contains(name):
        # add duplicates to list
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


"""
ANSWERS:

64 duplicates:

Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines,
Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs,
Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts,
Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias,
Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris,
Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre,
Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle,
Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto,
Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause,
Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran,
Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates,
Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach,
River Johnson, Ali Collier

runtime: 10.072882175445557 seconds

64 duplicates:

Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins,
Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine,
Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole,
Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins,
Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow,
Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman,
Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers,
Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris,
Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos,
Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo,
Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias,
Nelson Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs,
Megan Porter, Carsen Tyler, Jordin Schneider, Ralph Roth

runtime: 0.13416075706481934 seconds
"""
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# 1. Python has built-in tools that allow for a very efficient approach to this problem
# You can use the pandas library to do this. Pandas has a method called duplicate which can find duplicate rows

# What's the best time you can accomplish?
# I was able to go from a runtime of 10.072882175445557 seconds to a runtime of 0.13416075706481934 seconds.

# I want to try using a doubly linked list but do not have enough time