class Node:
    def __init__(self, value=None, next_node=None):
        '''Holds Node value'''
        self.value = value 
        '''references nxt Node'''
        self.next_node = next_node 

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        '''sets nxt Node refrence to whatever Node is passed in'''
        self.next_node = new_next 

class LinkedList:
    def __init__(self):
        ''' Head '''
        self.head = None 

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        '''Reference current Node , update as we iterate over list'''
        current = self.head 

        while current:
            if current.get_value() == value:
                '''Check if Node is valid , return True if Node value matches target value'''
                return True 

            '''update to point to next Node'''
            current = current.get_next() 

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return '...'
        prev = None
        cur = self.head
        nxt = self.head.get_next()

        while cur != None:
            cur.set_next(prev)
            prev = cur
            cur = nxt
            if nxt != None:
                nxt = cur.get_next()

        self.head = prev
