'''
When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer 
is overwritten with the newest element.

The append method adds the given element to the buffer.

The get method returns all of the elements in the buffer in a list in their given order
'''

# Create an empty buffer to hold the items that you append
# Add an identifier to the oldest item (first) in the buffer
# Simply append until you hit capacity
# After capacity is hit, replace the oldest item with the new item
    # then move the oldest_index identifier 1 place over to the next item.

# The get function only needs to return the current array we have stored


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Empty ring buffer to add items to
        self.buffer = []
        # Identifier to keep track of the oldest element, start at 0
        self.oldest_index = 0

    def append(self, item):
        # If capacity has not been reached, simply append the item to the buffer
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

        # If capacity has been reached, replace the oldest item with the new item
        # Update oldest_index to move one over, to the next oldest item
        else:
            # Replace oldest item with new item
            self.buffer[self.oldest_index] = item

            # Move oldest_index to the next item
            self.oldest_index += 1

        # The buffer only holds 5 items so it only has index values of 0-4
        # Once the oldest_index counter has moved past 4, it needs to be reset to 0
        if self.oldest_index == self.capacity:
            self.oldest_index = 0

    def get(self):
        # Return the current buffer
        return self.buffer
