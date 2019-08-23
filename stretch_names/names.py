import time

def binary_search(array, target): 
    lo = 0
    hi = len(array)
    mid = hi // 2
    while True:
      nm = array[mid]
      if (target > array[mid]):
        lo = mid
        mid = lo + (hi - lo) // 2
      elif (target < array[mid]):
        hi = mid
        mid = lo + (hi - lo) // 2
      else:
        return True
      if (mid >= hi or mid <= lo):
        return False

start_time = time.time()

f = open('/Users/wel51x/GDrive/Lambda/CS13/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/Users/wel51x/GDrive/Lambda/CS13/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2 = sorted(names_2)

duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
for name_1 in names_1:
    if binary_search(names_2, name_1):
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Original run time 9.513386964797974 seconds
# Improved run time 0.18606114387512207 seconds
# This run time 0.049501895904541016 seconds
