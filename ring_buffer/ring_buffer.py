class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] # start with an empty list
        self.oldestItem = 0 # declare the oldest item is at the 0 index

    def append(self, item):
        if len(self.storage) < self.capacity: # if there is some vacancies
            self.storage.append(item) # book a room
        else:
            self.storage[self.oldestItem] = item # if there are no vacancies, kick the first tenants out and replace with item
            if self.oldestItem < len(self.storage) - 1: # check to see who is the oldest
                self.oldestItem += 1 # move down the line
            else: #otherwise 
                self.oldestItem = 0 # kick the first tenant in the list out

    def get(self):
        return self.storage