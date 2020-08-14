class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_data = 0

    def append(self, item):
        # Check if the length of the list is less tha the capacity
        if len(self.storage) < self.capacity:
            # Append item to the end of the list
            self.storage.append(item)
        # If the list has reached capacity
        else:
            #Append the item by replacing the item at the oldest index
            self.storage[self.oldest_data] = item
            # Check if the oldest item is the last item in the list
            if self.oldest_data < len(self.storage) - 1:
                self.oldest_data += 1
            # If not, ncrement the oldest indext
            else:
            # Otherwise, reset oldest to first index
                self.oldest_data = 0


        #     # Check which item is the oldest
        #     if self.oldest_data < len(self.storage -1):
        #         # Increment the oldest_data value by 1
        #         self.oldest_data += 1
        #     else:
        #         # Or reset the oldest item to the first index
        #         self.oldest_data = 0 
        # elif len(self.storage) < self.capacity:
        #      # Append the passed item by replacing the item at the oldest index
        #     self.storage[self.oldest_data] = item
           

    def get(self):
        # Return the list
        return self.storage