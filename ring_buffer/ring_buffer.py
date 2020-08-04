class RingBuffer:
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.list = []
    	self.current_item_to_remove = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        elif len(self.list) == self.capacity:
            self.list.pop(self.current_item_to_remove)
            self.list.insert(self.current_item_to_remove, item)
            if self.current_item_to_remove < self.capacity - 1:
                self.current_item_to_remove += 1
            else:
                self.current_item_to_remove = 0

    	

    def get(self):
        return self.list