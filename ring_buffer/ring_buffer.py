class RingBuffer:
    def __init__(self, capacity):
    	self.capacity = capacity #set capacity
    	self.allItems = [] #create array
    	self.itt = 0 #create iterator

    def append(self, item):
    	if len(self.allItems) < self.capacity: #if th array's length is less then the capacity set
    		self.allItems.append(item)
    	else:
    		#if the length is = then switch the first 
    		#item for the second 1 the 1st time 
    		# and second value for new one, then the third nd so on
    		self.allItems[self.itt] = item
    		if (self.capacity - 1) == self.itt:
    			self.itt = 0
    		else:
    			self.itt += 1

    def get(self):
    		return self.allItems
