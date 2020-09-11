class RingBuffer:
    def __init__(self, capacity):
        self.q = list()
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def iterate_head(self):
        if self.head == self.capacity:
            self.head = 0
        else:
            self.head += 1

    def iterate_tail(self):
        if self.tail == self.capacity:
            self.tail = 0
        else:
            self.tail += 1

    def append(self, item):
        if len(self.q) == self.capacity:
            tail_item = self.q[self.tail]
            self.q.remove(tail_item)
            self.q.insert(self.tail, item)
            self.iterate_tail()
        else:
            self.q.insert(self.tail, item)
            self.iterate_tail()

    def get(self):
        start = self.head
        self.iterate_head()
        return_list = list()
        while self.head != start:
            item = self.q[self.head]
            if item:
                return_list.append(item)
            self.iterate_head()
        return return_list

