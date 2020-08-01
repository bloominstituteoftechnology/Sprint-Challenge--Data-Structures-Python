class Element:
    def __init__(self, id, val):
        self.id     = id
        self.value  = val

class RingBuffer:
    def __init__(self, capacity):
        self.capacity     = capacity        # defines the capacity of the ring buffer
        self.counter      = 0               # counter that serves as the id for new buffer elements
        self.queue_age    = []              # queue that keeps track of existing elements (oldest first)
        self.buffer       = []              # the actual buffer

    # has_room determines if there is excess capacity in the buffer
    def has_room(self):
        return len(self.buffer) < self.capacity

    # add_queue_age appends an element id to a queue keeping track of elements
    #   in terms of their age (oldest elements first)
    def add_queue_age(self, id):
        self.queue_age.append(id)

    # get_oldest_id pops the oldest element id and returns it
    def get_oldest_id(self):
        return self.queue_age.pop(0)

    # repl_item_id replaces the buffer item with the specified id
    #    with the given item
    def repl_item_id(self, id, item):
        found = False

        for i, elm in enumerate(self.buffer):
            if elm.id == id:
                found = True
                break

        if found:
            self.buffer[i] = item        

    # append appends a value to the buffer
    def append(self, val):
        # Create a new element instance
        self.counter    = self.counter + 1
        tmp_elm         = Element(self.counter, val)

        # Does the buffer have available capacity?
        if self.has_room():
            # Add the item to the stack
            self.buffer.append(tmp_elm)     # append the element to the buffer
            self.add_queue_age(tmp_elm.id)  # add the id to the age queue
            return
        
        if not self.has_room():
            # Identify the id of the oldest element
            id_old = self.get_oldest_id()

            # Remove the oldest element
            self.repl_item_id(id_old, tmp_elm)
            self.add_queue_age(tmp_elm.id)  
            return

    # get returns the current buffer in the form of a list of buffer values
    def get(self):
        ret_list = []

        # Iterate through our buffer
        for val in self.buffer:
            ret_list.append(val.value)

        return ret_list