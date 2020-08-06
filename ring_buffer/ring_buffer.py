class RingBuffer:
    def __init__(self,capacity): 
        self.capacity = capacity # capacity : max number in the buffer
        self.data = []     # empty storage for appending data later
        self.current_pos = 0  # current position index

        
    def append(self, x):
        # if the buffer not full, appending an element 'x' from the tail.
        if len(self.data) < self.capacity:
            self.data.append(x)

        # if the buffer is full, appending an element overwriting the oldest one. 
        else:
            self.data[self.current_pos] = x  # the oldest one's position starting from 0

        self.current_pos += 1  # then position plus 1
        self.current_pos = self.current_pos % (self.capacity)
        """
        if current_pos is smaller than capacity, the modulus return current_pos itself,
        if current_pos is bigger than capacity, the modelus trturn the reminders, and give it back to current_pos.
        for example: 2 % 8 = 2, 5 % 8 = 5, 8 % 8 = 0, 9 % 8 = 1.....
    
        """
        
        #This is another way to subtitute the modulus method above:
        """
        if self.current_pos == self.capacity:
            self.current_pos = 0
            
        """

    def get(self):
        # return list of elements in correct order 
        return self.data





