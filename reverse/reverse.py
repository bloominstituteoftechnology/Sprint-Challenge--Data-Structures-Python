class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Base Case if list is empty
        if self.head is None:
            return
        
        #swap previous and current
        prev_node = None
        current_node = self.head

        # Loop through all nodes
        while current_node is not None:
            # keep track of the next node
            upcoming = current_node.get_next()

            #overwrite next node with previous
            current_node.set_next(prev_node)

            #overwrite prev node with current
            prev_node = current_node

            # overwrite current node with original next node
            current_node = upcoming
        
        # make previous node the head
        self.head = prev_node
