class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur_pos = 0 

    def append(self, item):
        if len(self.data) < self.capacity:
             # Append an element overwriting the oldest one.
            self.data.append(item)
            # self.cur_pos += 1
        else:
            if self.cur_pos == self.capacity:
                self.cur_pos = 0
            self.data[self.cur_pos] = item
        self.cur_pos += 1
   
     
            
       
        # set data 'el' value to item
       
        
        

    def get(self):
        # return elements in order
        return self.data
        # pass