import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):	    
        if value < self.value:	       
            if self.left:	          
                self.left.insert(value)            
            else:	            
                self.left = BSTNode(value)	                
        else:	        
            if self.right: 	            
                self.right.insert(value)	                
            else:	           
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:	        
            return True	           
        if target < self.value:	        	            
            if self.left is None:	            
                return False	                
            else:	            
                return self.left.contains(target)	                
        else:  	         
            if self.right is None:	            
                return False	               
            else:	            
                return self.right.contains(target)

# rewrote the code from earlier modules this week for the BTSNode
# and modified the for loop to insert the names into the BTSnode
# and append 'duplicates' if btsnote already contains it.


# both tests contained 64 dupes in 'duplicates', and
# the first test had over 7 seconds runtime, final test had 1/10 second.

bts = BSTNode('')

for n in names_1:
    bts.insert(n)
for n in names_2:
    if bts.contains(n):
        duplicates.append(n)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


'''
python names/names.py
'''