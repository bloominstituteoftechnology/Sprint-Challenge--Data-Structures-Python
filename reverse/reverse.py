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
    """LL Class"""
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

    def iterative_reverse_list(self, node, prev):
        """
        Reverse the contents of the list using recursion, not a loop
        """
        # Used while loop to get working solution, came back and added
        # recursive solution later

        if self.head is None:
            return None

        # Start with head
        self.head = node
        current = self.head
        # Define next node
        nn = current.next_node

        # if there is a next node
        while nn is not None:
            # establish previous
            prev = current
            # make next node the new current
            current = nn
            nn = current.next_node
            # reversal
            current.next_node = prev

            # if no next nodes
            if nn is None:
                # whatever was current will be the head
                self.head = current

    def reverse_list(self, node, prev):
        """
        Reverse the contents of the list using recursion, not a loop
        """
        # Recursive solution without loop:

        # If there is no node, then declare the previous node as the head node
        if node is None:
            self.head = prev
        # if there is a node ...
        else:
            # call the reverse_list method on the node's next, with the current
            # node as the previous
            self.reverse_list(node.next_node, node)
            node.next_node = prev

if __name__ == "__main__":

    ll = LinkedList()

    ll.add_to_head(1)
    ll.add_to_head(2)
    ll.add_to_head(3)
    ll.add_to_head(4)
    ll.add_to_head(5)

    # breakpoint()
    ll.reverse_list(ll.head, None)
    print(ll.head.value) #> 1
    print(ll.head.get_next().value) #> 2
    print(ll.head.get_next().get_next().value) #> 3


    # breakpoint()