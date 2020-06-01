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
        
    def __str__(self):
        return f'{self.value}'

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
    
    def traverse(self):
        current = self.head
        
        while current:
            print(current)
            current = current.next_node

    def reverse_list(self, node, prev):
        pointer = self.head

        while pointer:
        # hold next node 
            next = pointer.next_node

        # delete the current pointer.next
            pointer.next_node =  prev

        #assing prev to the current pointer
            prev = pointer

        # step to next node
            pointer = next
        
        self.head = prev


# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# list.add_to_head(6)
# list.reverse_list(list.head, None)
# list.traverse()