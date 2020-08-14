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
        # current value
        curr_node = self.head
        # hold value to switch
        previous_node = None

        # keep going through items until we reach the end
        while curr_node is not None:
            # keep as the current node's next
            next_node = curr_node.get_next()
            # set the current's next to previous
            curr_node.set_next(previous_node)
            
            # update previous to updated current
            previous_node = curr_node
            # update previous to be current for next iteration
            curr_node = next_node
        
        # after looping is done, set the head to the last node
        self.head = previous_node