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
        
        # empty list case
        if node is None:
            pass

        else:
            # bottom out here - this'll be the new head
            if node.get_next() is None:
                #set the node's next to be the previous node
                node.set_next(prev)

                # set the head
                self.head = node

            else:
                # call the function on the next node, with the current node as it's previous.
                self.reverse_list(node.get_next(), node)
                
                # set the node's next to be the previous node
                node.set_next(prev)

# I'm pretty certain time complexity here is O(n). The number of function calls are proportional 
# to the number of elements in the list.