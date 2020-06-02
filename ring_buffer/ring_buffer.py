class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.store = (None) * capacity
        self.index = -1

    def append(self, item):
        if item is not None:
            # Fill buffer
            if len(self.store) < self.capacity:
                self.store.append(item)
            # Re-write buffer in order
            else:
                index = self._get_active()
                # print(index)  # DEBUG
                self.store[index] = item

    def _get_active(self):
        if self.index < self.capacity - 1:
            self.index += 1
            return self.index
        else:
            self.index = 0
            return self.index

    def get(self):
        return [item for item in self.store if item is not None]



if __name__ == "__main__":
    buffer = RingBuffer(3)
    for item in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        buffer.append(item)
        print(buffer.get())