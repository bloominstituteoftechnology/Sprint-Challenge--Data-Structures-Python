"""
Task 1. Implement a Ring Buffer Data Structure

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full 
and a new element is inserted, the oldest element in the ring buffer is overwritten with 
the newest element. This kind of data structure is very useful for use cases such as 
storing logs and history information, where you typically want to store information up 
until it reaches a certain age, after which you don't care about it anymore and don't mind 
seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. 
The append method adds the given element to the buffer. The get method returns all of the 
elements in the buffer in a list in their given order. It should not return any None 
values in the list even if they are present in the ring buffer.
"""

class RingBuffer:
    """
    a queue with a max size that loops back over itself
    FIFO(?)
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0  
        self.storage = [None] * capacity

    def append(self, item):
        """
        append method adds the given element to the end of the buffer (not replaces it if full?)
        """
        self.storage[self.index] = item
        self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        """
        get method returns list of all non-none elements from oldest to newest
        """
        return [item for item in self.storage if item is not None]

# but why do this instead of dequeu/enqueu operations?