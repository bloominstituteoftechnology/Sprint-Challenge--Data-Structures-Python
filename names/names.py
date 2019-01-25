import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

cache = {}
duplicates = []
def cachefunc(cache = {}, duplicates = []):
    for i in range(0, len(names_1)):
        if names_1[i] == names_2[i]:
            duplicates.append(names_1)
    return duplicates

print(cachefunc())
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

#!/usr/bin/python

# import sys
# # count = 0
# # x = 0
# def climbing_stairs(n, cache={}):
#   #nCr = n!/r!(n-r)!

#   if n < 0:
#     return 0
#   if n == 0:
#     return 1
#   if n == 1:
#     return 1
#   if n == 2:
#     return 2
#   if n == 3:
#     return 4
#   if n == 4:
#     return 7

#   if n in cache:
#     return cache[n]

#   nth = climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
#   cache[n] = nth
#   return nth