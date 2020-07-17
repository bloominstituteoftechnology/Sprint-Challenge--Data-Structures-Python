from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # this is a constructor list which will take a parameter capacity and iterate til the end
        self.items = list()[-capacity:]
        self.ring_position = 0



    def append(self, item):
       # if the len of the items is equal to the capacity then we will equalize the position of items by the position
       # numbe of the ring to the item
       # so what we are trying to do here is to be able to give an index to the item by the order
       # so if we try to call the buffer by the index we should receive the result of the demanded item.
       if len(self.items) == self.capacity:
           self.items[self.ring_position] = item
        # here after any case > or < or whatever we are going to append the item to the items
       else:
           self.items.append(item)




    def get(self):
        return self.items