class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # create a list to store the items
        self.list_items = []
        # set the first index
        self.index = 0

    def append(self, item):
        """Append an element overwriting the oldest one"""
        # if the list didn't reach the full capacity
        # add item to the end of list
        if len(self.list_items) != self.capacity:
            self.list_items.append(item)
        # if the list reached the full capacity
        else:
            # 
            self.list_items[self.index] = item
        # increase the index and limit the values it may take
        # 0-4
        self.index = (self.index + 1) % self.capacity

    def get(self):
        """Returns the list of items"""
        return self.list_items