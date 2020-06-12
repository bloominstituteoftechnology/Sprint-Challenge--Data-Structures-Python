class Node: 
    def __init__(self, value = None, next_node = None ):
        self.value = value
        self.next_node = next_node 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.first_node = None
        self.last_node = None

    def append(self, item):
        if self.size == self.capacity:
            self.pop()

        self.size += 1

        new_node = Node(item)

        if self.first_node == None:
            # First element 
            self.first_node = new_node
            self.last_node = new_node
            return 

        self.last_node.next_node = new_node
        self.last_node = new_node

    def pop(self):
        if self.size == 0:
            return None

        remove_first_node = self.first_node
        self.first_node = remove_first_node.next_node
        remove_first_node.next_node = None

        self.size -= 1

        if self.size == 0:
            self.first_node = None
            self.last_node = None

        return remove_first_node.value

    def get(self):
        current_item = self.first_node
        entire_buffer = []
        while True:
            entire_buffer.append(current_item.value)
            if current_item == self.last_node:
                break
            current_item = current_item.next_node

        return entire_buffer

