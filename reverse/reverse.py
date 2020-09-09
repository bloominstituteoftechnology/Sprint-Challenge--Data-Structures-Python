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
        # Iterative solution
        # initialize 3 pointers. Prev = Null, curr = head, next is null 
        prev = None
        current = self.head 
        # store the next node before changeing it
        # change the next pointer to previous. this is where it does reverse
        # move prev and current 1 step ahead
        # repeat process till current node is not null. 
        while current:
            next = current.next_node
            current.next_node = prev
            prev=current
            current=next
        self.head=prev


