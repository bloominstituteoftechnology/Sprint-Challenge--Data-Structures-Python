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
        pass

    def get(self):
        pass