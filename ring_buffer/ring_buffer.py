class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 # current space
        self.storage = [None] * capacity # setting storage limit


    def append(self, item):
        # if there is available space
        if self.current < self.capacity:
            # append item without deleting older item
            self.storage[self.current] = item
            self.current += 1
        else:
            # if there is not enough space
            self.current = 0 # replace the oldest item idx 0, with the new item
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        items = []

        # adding items that are not None
        for item in self.storage:
            if item != None:
                items.append(item)

        return items

        # return [i for i in self.storage if i != None ] can write as a list comprehension

if __name__ == "__main__":
    # Running test to see if it works
    # set capacity to 3

    buffer = RingBuffer(3)

    print(buffer.get())   # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    print(buffer.get())   # should return ['a', 'b', 'c']

    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    print(buffer.get())   # should return ['d', 'b', 'c']

    buffer.append('e')
    buffer.append('f')

    print(buffer.get())   # should return ['d', 'e', 'f']

"""
ANSWERS
[]
['a', 'b', 'c']
['d', 'b', 'c']
['d', 'e', 'f']



TEST
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
"""