class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.current = 0


# The append method adds the given element to the buffer
# The get method returns all of the elements in the buffer in a list in their given order.
# It should not return any None values in the list even if they are present in the ring buffer


    def append(self, item):
        # okay first we need to see if we can append to the current capaity
        if len(self.data) < self.capacity:
            self.data.append(item)

        elif self.current == self.capacity:

            self.current = 0
            self.data[self.current] = item

        else:
            self.data[self.current] = item
        self.current += 1

    def get(self):
        return self.data


buffer = RingBuffer(3)


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


# Write out our algorithm as pseudocode.

# the FUCKING PROBOLEM
# bitches have ran out of cap
# when a new things gets added in we need to ake out the oldest thing
# which it should alays be the one at index 0 RIGHT????

# PSEUDOCODE


# Change each line of pseudocode into actual code.
# Test out our code and see if it is returning the outputs that we would expect.
