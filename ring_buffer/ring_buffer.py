class RingBuffer:
    # this implements a buffer that isn't full yet
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        # the oldest item is at the 0 index
        self.oldest_item = 0


    def append(self, item):
        # if the storage is less than the total capacity
        if len(self.storage) < self.capacity:
            # append the item
            self.storage.append(item)
            # if there storage isn't less than the total capacity
        else:
            # "append" an item by overwriting the oldest item
            self.storage[self.oldest_item] = item
            # verify which item is the oldest
            if self.oldest_item < len(self.storage) - 1:
                # increment by 1 so we can go through the list
                self.oldest_item += 1
            else:
                # remove the first item or "oldest" item in the list
                self.oldest_item = 0

    def get(self):
        # returns a list of elements from the oldest to the newest
        return self.storage