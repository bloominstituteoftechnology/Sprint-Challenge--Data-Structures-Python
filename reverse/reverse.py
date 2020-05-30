class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value # the value at this linked list node
        self.next_node = next_node # reference to the next node in the list

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next # set this node's next_node reference to the passed in node

class LinkedList:
    def __init__(self): #default for LL
        self.head = None #head of list

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
        if(node is None):
            return

        elif node.next_node is None :
            p = prev
            self.head = node
            node.next_node = prev
            return

        self.reverse_list(node.next_node, prev=node)
        p = prev
        node.next_node = prev
        return
