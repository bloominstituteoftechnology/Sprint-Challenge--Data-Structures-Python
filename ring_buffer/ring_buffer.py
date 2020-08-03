class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.position_in_queue = 0

    def append(self, item):
        """Appends an element to the buffer.
        If appending beyond the buffer's maximum
        capacity, the new items will loop back
        over the buffer, overwriting old values.
        """
        # Add item to buffer if below the maximum capacity
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # set pointer for the current position in the buffer
            self.storage[self.position_in_queue] = item
        # Increase to next position in the buffer
        self.position_in_queue += 1
        # If the position is the last value based on maximum capacity,
        # reset the position to zero, overwriting the old value(s).
        if self.position_in_queue == self.capacity:
            self.position_in_queue = 0

    def get(self):
        """Returns a list of elements in the buffer"""
        return self.storage


buffer = RingBuffer(3)
buffer.get()
buffer.append("a")
buffer.append("b")
buffer.append("c")
buffer.append("d")
print(buffer.get())
buffer.append("e")
buffer.append("f")
print(buffer.get())
