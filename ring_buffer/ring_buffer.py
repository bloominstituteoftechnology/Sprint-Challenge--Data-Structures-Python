class RingBuffer:

    # Queue using a list instead of linked list because am lazy
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = list()
        self.size = 0
        self.last_added_index = 0

    # adds the given element (item) to the buffer
    def append(self, item):

        # if you hit max capacity, replace oldest item with newest
        if self.size >= self.capacity:
        
            # replace oldest item with newest using old item's index
            self.storage[self.last_added_index] = item

            # set new last_added_index
            self.last_added_index += 1

            # reset the index counter when incrementer goes outside of range
            if self.last_added_index == self.capacity:
                self.last_added_index = 0

        else:
        # add item to end of list
            self.storage.append(item)
        
        # only increment buffer size property if it's not at capacity
        if self.size < self.capacity:
            self.size += 1

    # returns all the elements in the buffer in a list in their given order
    # it should not return and None values in the list even if they're present
    def get(self):
        
        # only fills in list of items if they are not None
        new_list = [item for item in self.storage if item]
        return new_list