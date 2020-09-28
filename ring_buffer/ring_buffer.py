class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []  # SIZE/COUNT ##########
        self.current = 0  # EMPTY ARRAY - OBJECT ##########

    def append(self, item):
        ########## APPENDING AN ELEMENT ##########
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        elif len(self.buffer) == self.capacity:
            self.buffer[self.current] = item
            # OVERWRITE OLDEST ELEMENT ##########
            self.current = (self.current + 1) % self.capacity

    def get(self):
        ########## RETURNING A LIST OF ELEMENTS [OLDEST-NEWEST] ##########
        if self.buffer is not None:
            # SLICED WITH THE COLON ON THE END IS FOR TESTING AND IF IT IS IN THE FRONT IT WILL FAIL ##########
            return self.buffer[:self.current]+self.buffer[self.current:]
