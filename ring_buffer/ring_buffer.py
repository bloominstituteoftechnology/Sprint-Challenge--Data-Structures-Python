class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.structure = []
        self.structure_index = 0

    def append(self, item):
        # fill array once
        if len(self.structure) < self.capacity:
            self.structure.append(item)
      
        else:
            # make sure the index isn't the same size of capacity 
            if self.structure_index < self.capacity:
                #remove the previous item
                self.structure.pop(self.structure_index)
                # add to the structure
                self.structure.insert(self.structure_index, item)
                #increase index by one
                self.structure_index += 1
            else: 
                #reset to zero
                self.structure_index = 0
                # remove from index
                self.structure.pop(self.structure_index)
                # add to the structure
                self.structure.insert(self.structure_index, item)
                #increase index by one
                self.structure_index += 1

    def get(self):
        return self.structure