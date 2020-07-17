from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # this is a constructor list which will take a parameter capacity and iterate til the end
        self.items = list()[-capacity:]
        self.ring_position = 0



    def append(self, item):
       # if the len of the items is equal to the capacity then we will append items with its position
       # to the item
       if len(self.items) == self.capacity:
           self.items[self.ring_position] = item
           # if the items are lesser then capacity then we will append the item to items as new item.
       if len(self.items) < self.capacity:
           self.items.append(item)





    def get(self):
        return self.items