import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# was researching ways to compair lists on python and this site
# https://realpython.com/python-sets/
# probably about 1/3 of the way down talks about compairing dubplicates using sets, they are unordered and since set items are unique, no duplicates are allowed which made this assignment much easier but the elements contained are immutable which means it cannot be changed so elemtns like int, float, bool, string, and tuples etc.  So when adding a list it becomes immutable which might limit the overal use of the this function i'm guessing

# using the operation 'name_1.intersection(name_2)' or 'name_1 & name_2' and will print out the duplicates


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = set(names_1) & set(names_2)

# which ran it down to 0.005 seconds or 0.006 if rounding up

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

