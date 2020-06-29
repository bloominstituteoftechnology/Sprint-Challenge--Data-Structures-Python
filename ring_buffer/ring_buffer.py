"""
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer
is full and a new element is inserted, the oldest element in the ring buffer
is overwritten with the newest element. This kind of data structure is very
useful for use cases such as storing logs and history information, where you
typically want to store information up until it reaches a certain age, after
which you don't care about it anymore and don't mind seeing it overwritten by
newer data.
"""


class RingBuffer:
    """
    A class for fixed-size buffers.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        """
        The append method adds the given element to the buffer.
        """
        self.storage[self.index] = item
        self.index = (self.index + 1) % len(self.storage)

    def get(self):
        """
        The get method returns all of the elements in the buffer in a list in
        their given order. It should not return any None values in the list
        even if they are present in the ring buffer.
        """
        return [item for item in self.storage if item is not None]
