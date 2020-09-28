class RingBuffer:
    def __init__(self, capacity):
        # setup max capacity and storage
        self.capacity = capacity
        self.storage = []
        # initialize ring buffer size to zero
        self.size = 0
        # instantiate head to update
        self.head = 0  # to equal oldest element

# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
# class _ _Full:
#         """ class that implements a full buffer """
#         def append(self, x):
#             """ Append an element overwriting the oldest one. """
#             self.data[self.cur] = x
#             self.cur = (self.cur+1) % self.max

    def append(self, item):
        # first check if the storage is full
        if self.size == self.capacity:
            # replace index at self.head
            self.storage[self.head] = item

            # update head to be oldest item in storage. When this leaves no remainders start back at 0
            self.head = (self.head + 1) % self.capacity

        # otherwise if storage is not full enqueue item
        else:
            self.enqueue(item)

    def get(self):
        # returns all of the elements in the buffer in a list
        return self.storage

    # Added enqueue to insert values at end of RingBuffer.
    def enqueue(self, value):
        # inserts the value at the end of the storage
        self.storage.append(value)
        # increases size by 1
        self.size += 1
