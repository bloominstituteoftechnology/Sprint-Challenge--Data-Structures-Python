import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# original runtime: 15.54635500907898 seconds
#for name_1 in names_1:
    #for name_2 in names_2:
        #if name_1 == name_2:
            #duplicates.append(name_1)

#runtime: 0.021982908248901367 seconds
names_2_dict = {}

for name_2 in names_2: ##check if the name is in the list if it is show true 
    names_2_dict[name_2] = True

for name_1 in names_1:## check the name string is in the list
    if name_1 in names_2_dict:## if string is in name 2 dict 
        duplicates.append(name_1)## append duplicates 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
