class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index =0
        self.size =0

    def append(self, item):
        # self.data.append(item)
        if self.size >= self.capacity:
        	self.data[self.index] = item
            #  self.size += 1
        else:    
            self.data.append(item)
            self.size += 1

        if self.index < (self.capacity -1):
            self.index +=1
            print('append', self.data)
        else:
            self.index = 0

    def get(self):
        while self.data:
        	print('I got', self.data)
        	return self.data

buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')
buffer.append('l')
buffer.append('m')


buffer.get()