class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        prev = None  # Keeps track of previous node
        cur = self.head  # Initial head of the list, moves along as we go through the list
        while cur:  # while current node is not equal to null...
            nxt = cur.next_node  # goes to the next node before changing the pointer
            cur.next_node = prev  # Flips the pointers to the previous node
            prev = cur  # updates the previous node to the current node
            cur = nxt  # the current node should be updated to the next one its going to
        self.head = prev

    # A -> B -> C -> D -> Null(0) flip into...
    # D -> C -> B -> A -> 0

    # A <- B <- C <- D <- 0 We're flipping the pointers
    # Iterate through the list while keeping track going through the node
