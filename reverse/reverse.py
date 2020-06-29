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
        # use recursion to solve this problem
        # check if the list is empty
        if node is None:
            return "It's an empty list"
        # store the node's next points to a new variable   
        current_next = node.get_next()
        # reverse, set the node's next points to his prev
        node.set_next(prev)
        
        # if current node is not the tail, continue the recursion,
        # and reverse the points: node = current_next, prev = node...
        if current_next is not None:
            self.reverse_list(current_next,node)
        # if the current node is the tail, set it head...
        else:
            self.head = node
