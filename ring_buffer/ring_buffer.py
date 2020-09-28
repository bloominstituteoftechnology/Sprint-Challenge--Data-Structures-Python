class RingBuffer:
    def __init__(self, capacity):
        # setup max capacity and storage
        self.capacity = capacity
        self.storage = []
        # setup size to zero
        self.size = 0
        # instantiate the tail and head to insert and remove oldest and newest
        self.tail = -1 # to equal newest element
        self.head = 0 # to equal oldest element


    def append(self, item):
        # first check if the storage is full
        if self.size == self.capacity
            # if full enqueue the item to the tail

            # decrease the size 

            # otherwise enqueue the item

    def get(self):
        # returns all of the elements in the buffer in a list
        return self.storage