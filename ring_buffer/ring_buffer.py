class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.oldest_index = 0

    def append(self, item):
        """
        Adds the given item to the buffer
        """
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list[self.oldest_index] = item
            if self.oldest_index < len(self.list) - 1:
                self.oldest_index += 1
            else:
                self.oldest_index = 0

    def get(self):
        """
        Returns all of the elements in the buffer, as a list, in their given order.
        Does not return any None values in the list, even if they are present in the ring buffer.
        """
        return [item for item in self.list if item]