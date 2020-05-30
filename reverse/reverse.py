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
        current_position = self.head # START AT THE HEAD OF THE LINKED LIST
        next_node = None # SET THE VALUE OF 'NEXT' TO 'None' TO START
        prev = None # THERE IS NO 'PREVIOUS' TO POINT TO, YET 
        
        while current_position is not None:
            next_node = current_position.next_node # POINT THE VALUE OF THE NEXT NODE TO BE VALUE OF THE NEXT NODE
            current_position.next_node = prev # REVERSE THE POINTER FOR NEXT TO BE PREVIOUS  
            prev = current_position # CHANGE POINTER FROM 'PREVIOUS' TO 'CURRENT'
            current_position = next_node # CHANGE POINTER FROM 'CURRENT' TO 'NEXT'
        self.head = prev
