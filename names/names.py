import time
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
# Original First Pass
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

# Second Pass
duplicates = list(set(names_1) & set(names_2))
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

"""
First Pass
64 duplicates:
Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier
runtime: 6.527417898178101 seconds
"""
"""
Second Pass
duplicates = list(set(names_1) & set(names_2)) # the same as duplicates = list(set(names_1).intersection(set(names_2)))
64 duplicates:
Grace Bridges, Ashlee Randall, Eden Howe, Peyton Lloyd, Dashawn Green, Carsen Tyler, Logan Morrow, Sanai Harrison, Piper Hamilton, Andre Carrillo, Aydan Calderon, Franklin Cooper, Giancarlo Warren, Luciana Ford, Ahmad Watts, Jaydin Sawyer, Alvaro Robbins, Lennon Hunt, Kameron Osborne, Aleah Valentine, Megan Porter, Marley Rivers, Jadyn Mays, Hallie Vazquez, Nathalie Little, Dulce Hines, Pablo Berg, Justine Soto, Raven Christensen, Nelson Acevedo, Trace Gates, Abel Newman, Kale Sawyer, Irvin Krause, Leon Cochran, Addison Clarke, Devyn Aguirre, Daphne Hamilton, William Maldonado, Maliyah Serrano, Camryn Doyle, Jordin Schneider, Marisol Morris, Cloe Norris, Davion Arias, Josie Dawson, Zara Suarez, Ralph Roth, Clay Wilkinson, Ali Collier, Leia Foley, Winston Austin, Salma Meza, Carley Gallegos, Jaden Hawkins, Malcolm Nelson, Victoria Roach, Selah Hansen, Malcolm Tucker, Josie Cole, Diego Chaney, River Johnson, Amiah Hobbs, Hayley Morgan
runtime: 0.005264997482299805 seconds
"""