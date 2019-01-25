import time

"""
Stretch Goal: Implement using arrays
"""

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#duplicates = []
#
#for name_1 in names_1:
#	for name_2 in names_2:
#		if name_1 == name_2:
#			duplicates.append(name_1)
					
duplicates = []
name_array = []

"""
Here, I implemented two internal methods (binary_search and binary_insert) to help with sorting out the names into a name_array, then check if the name we're interested in is in the sorted name_array. If it is, then it's a duplicate and we append it to the duplicates array.
"""

def binary_search(arr, target):	# O(log(n))

	"""
	This method finds if the "target" is in the array; if it is, then it's going to return the index.
	"""
	if len(arr) == 0:
		return None # array empty
		
	low = 0
	high = len(arr)-1

	while low <= high:
		middle = (low + high) // 2
		
		if arr[middle] == target:
			return middle
		elif arr[middle] > target:  # If target is less than the middle, ignore the right side
			high = middle - 1
		else:
			low = middle + 1
		
	return None # not found


def binary_insert(arr, target):	# O(log(n))
	
	"""
	This method finds if where in the array the "target" should be and insert it.
	"""
	if len(arr) == 0:
		arr.insert(0, target)
		return 0 # array empty
		
	low = 0
	high = len(arr)-1

	while True:
		middle = (low + high) // 2
		
		if arr[middle] == target:
			arr.insert(middle, target)
			return middle
		elif arr[middle] > target:  # If target is less than the middle, ignore the right side
			high = middle - 1
		else:
			low = middle + 1
			
		if low > high:
			arr.insert(low, target)
			return low

"""
Call the binary methods in the loop.
"""

for name_1 in names_1:	# O(n log n)
	binary_insert(name_array, name_1)	# O(log n)
	
for name_2 in names_2:	# O(n log n)
	if binary_search(name_array, name_2) is not None:	# O(log n)
		duplicates.append(name_2)	# O(1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


"""
The runtime complexity is O(2 * n log(n)) => O(n log(n)).
	Reasoning: We now have two separate loops, each with a binary-search-tree method of O(n log(n)), since the loop itself is O(n), and when combined the overall operation of each loop is O(n log(n)). Since there are two loops, its O(n log(n)) * 2 => O(2 * n log(n)) =>  O(n log(n))
	
The space complexity is O(n), which is the same as the complexity in my original solution. 

=> Overall, comparing this algorithm to my original solution (using a set()), the solution with the set() is better because it is O(n).

"""