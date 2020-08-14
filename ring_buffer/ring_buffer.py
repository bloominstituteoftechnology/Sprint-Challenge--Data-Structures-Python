class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.index = 0


# The append method adds the given element to the buffer
# The get method returns all of the elements in the buffer in a list in their given order.
# It should not return any None values in the list even if they are present in the ring buffer


    def append(self, item):
        # dont PANIC --- calm down!! Youve got this.
        # okay first we need to see if we can append to the current capaity
        if len(self.data) < self.capacity:
            self.data.append(item)
            # adding an element when the this is full replaces the 1st one and 2nd repleaces the 2nd one

        # append the item and remove the first item
        else:
            self.data.pop(0)
            self.data.append(item)

    def get(self):
        return self.data

        # if len(self.data) >= self.capacity:
        # we need to make it so that adds in order by index. so that when the first one is added in it is then 0 then #2 becomes 1

        # ughh i have no idea how to do that.


buffer = RingBuffer(3)

# nice working! proud of myself? who knows

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')
buffer.append('g')

buffer.append('h')

buffer.append('i')

buffer.append('j')


buffer.get()   # should return ['h', 'i', 'j']
