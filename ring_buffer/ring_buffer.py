class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = list()
        self.index_on_deck = 0

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items.pop(self.index_on_deck)
            self.items.insert(self.index_on_deck, item)
            if self.index_on_deck == self.capacity - 1:
                self.index_on_deck = 0
            else:
                self.index_on_deck += 1

    def get(self):
        return [b for b in self.items]