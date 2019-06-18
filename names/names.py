import time
#from functools import lru_cache

#@lru_cache(maxsize=0)
def namez():
    start_time = time.time()

    f = open('names_1.txt', 'r')
    names_1 = f.read().split("\n")  # List containing 10000 names
    f.close()

    f = open('names_2.txt', 'r')
    names_2 = f.read().split("\n")  # List containing 10000 names
    f.close()
      
    
    def match(arr, name_1, leftIndex, rightIndex):
        # Base case 
        if leftIndex >= rightIndex:
            return leftIndex

        # Finding the midpoint
        midpoint = leftIndex + (rightIndex - leftIndex) // 2

        # Go right if index and value match
        if arr[midpoint] < name_1:
            return match(arr, name_1, midpoint + 1, rightIndex)

        # Go left if index and value do not match
        elif arr[midpoint] > name_1:
           return match(arr, name_1, leftIndex, midpoint - 1)

        else:
          if arr[midpoint] == name_1:
            duplicates.append(name_1)  
    
    duplicates = []
    #names_1.sort()
    names_2.sort()
    for name_1 in names_1:
        match(names_2, name_1, 0, len(names_2) - 1)
   
    end_time = time.time()
    print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
    print (f"runtime: {end_time - start_time} seconds")

namez()