class RingBuffer:
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.data = []
    	self.age = 0

    def append(self, item):    
    	
        if len(self.data) < self.capacity: # buffer not full
            self.data.append(item)
        else: # Buffer is full
        	self.data[self.age] = item

        self.age += 1

        if self.age == self.capacity: # end of array, go to start
        	self.age = 0

    def get(self):
        return self.data