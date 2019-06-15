import time
from functools import lru_cache

@lru_cache(maxsize=0)
def namez():
    start_time = time.time()

    f = open('names_1.txt', 'r')
    names_1 = f.read().split("\n")  # List containing 10000 names
    f.close()

    f = open('names_2.txt', 'r')
    names_2 = f.read().split("\n")  # List containing 10000 names
    f.close()
      
    #duplicates = []
    #names_1.sort()
    #names_2.sort()
    
    def match(arr, name1, leftIndex, rightIndex):
        # Base case 
        if leftIndex >= rightIndex:
            return leftIndex

        # Finding the midpoint
        midpoint = leftIndex + (rightIndex - leftIndex) // 2

        # Go right if index and value match
        if arr[midpoint] < name1:
            return match(arr, name_1, midpoint + 1, rightIndex)

        # Go left if index and value do not match
        elif arr[midpoint] > name1:
           return match(arr, name_1, leftIndex, midpoint - 1)

        else:
          duplicates.append(name_1)  
    
    duplicates = []
    names_1.sort()
    names_2.sort()
    for name_1 in names_1:
        match(names_2, name_1, 0, len(names_2))
    
    #while x < names_1.len():
    #for name_1 in names_1:
    #    name_1 = names_1[x]
    #    while names_2 is not None:
    #        mid = floor(names_2.len()) / 2
    #        name_2 = names_2[mid]
    #        if name_2 = name_1:
    #            duplicates.append(name_1)   
    #        elif name_1 < name_2:
    #            mid
        
    #    left = names_2.splice(0
    #    right = names_2[mid+1:]
    #    name_2 = names_2[mid]
    #    if name_2 = name_1:
    #        duplicates.append(name_1)   
    #    elif name_1 < name_2:
    #        mid
            
        
    #    for name_2 in names_2:
    #        mid = floor(names_2.len()) / 2
    #        left = names_2[:mid]
    #        right = names_2[mid+1:]
    #        if        
    #        if name_1 == name_2:
    #            duplicates.append(name_1)

    end_time = time.time()
    print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
    print (f"runtime: {end_time - start_time} seconds")

namez()