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
        # Do we have an empty list?
        if self.head == None:
            # empty list -> nothing to do
            return

        # Do we have a list with just one element?
        if self.head != None and self.head.next_node == None:
            # just one element -> also nothing to do
            return

        #* Processing a linked list with at least 2 elements
        # Create a work list
        wrk_list     = []
        wrk_list_ctr = 0
        cntnu        = True

        # Traverse the linked list and append element references to the list
        cur_node = self.head
        while cntnu:
            wrk_list.append(cur_node)
            wrk_list_ctr = wrk_list_ctr + 1

            # Is this the last node in the linked list? Break out of the process
            #   (next_node == None)
            if cur_node.next_node == None:
                break

            # Have more elements in the linked list to process
            cur_node = cur_node.next_node
        
        # Have our work list populated
        # Reverse the work list
        wrk_list.reverse()

        # Iterate through the reversed list
        for idx, elm in enumerate(wrk_list):
            # Are we at the first element in the reversed list? (this is the new head)
            if idx == 0:
                self.head = elm # Set the new head value
                continue

            # Handling a post head element
            #   make sure the previous element links to the current element
            wrk_list[idx-1].next_node = elm

            # Are we at the last element in the reversed list?
            if idx == wrk_list_ctr - 1:
                elm.next_node = None

