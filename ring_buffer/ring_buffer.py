class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Set the new item that is passed in to evaluate to the current item in storage
        self.storage[self.current] = item
        # if the current value is less than the overall capasity.
        if self.current < self.capacity - 1:
          # add it to the list
            self.current += 1
        else:
          # otherwise set current to evaluate to 0
            self.current = 0

    def get(self):
        list = []
        for value in self.storage:
            if value is not None:
                list.append(value)
        return list


# A ring buffer is a non-growable buffer with a fixed size.
# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
# This kind of data structure is very useful for use cases such as storing logs and history information,
# where you typically want to store information up until it reaches a certain age,
# after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# The `append` method adds elements to the buffer.
# The `get` method returns all of the elements in the buffer in a list in their given order.
# It should not return any `None` values in the list even if they are present in the ring buffer.
