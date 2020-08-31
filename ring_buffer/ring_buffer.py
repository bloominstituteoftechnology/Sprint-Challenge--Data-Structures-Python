# initialize variable
# Needs to hol the data
# Index variable with value of 0 to start

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_data = 0

    def append(self, item):
        # Check if length of the list is less than the capacity
        # Append item to the end of the list
        # 1. If the list has reached capacity
        # a. Append the item by replacing the item at the oldest index
        # b. Check if the oldest item is the last item in the list
        # c. If not increment the oldest index
        # d. Otherwise reset oldest to first index
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldest_data] = item
            if self.oldest_data < len(self.storage) -1:
                self.oldest_data += 1
            else:
                self.oldest_data = 0

# Return the list
    def get(self):
        return self.storage