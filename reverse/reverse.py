class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        if self.next_node is None:
            next_val = None
        else:
            next_val = self.next_node.value
        return f'Value: {self.value} Next: {next_val}'

    def get_next(self):
        return self.next_node

    @property 
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, new_node):
        self.__next_node = new_node


# Global Stack
gstack = []


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        

    def add_to_head(self, value, isnode=False):
        if not isnode:
            node = Node(value)
        else:
            node = value

        try:
            if self.head is not None:
                node.next_node = self.head
        except:
            pass

        self.head = node


    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.value == value:
                return True
            # update our current node to the current node's next node
            current = current.next_node
        # if we've gotten here, then the target node isn't in our list
        return False


    def reverse_list(self):

        def _traverse_store(node, stack):
            if node is not None:
                stack.append(node)
                # print('Stack size', len(stack))
                if node.next_node is not None:
                    # print(f'Traversing/Store {node.value}')
                    next_node = node.next_node
                    node.next_node = None
                    _traverse_store(next_node, stack)

        def _rewrite_head(stack):
            if len(stack) > 0:
                # print('making new head')
                new_head = stack.pop(0)
                self.head = new_head

        def _rewrite_self(stack):
            if len(stack) > 0:
                self.add_to_head(stack.pop(0), isnode=True)
                _rewrite_self(stack)

        stack = gstack
        _traverse_store(self.head, stack)
        _rewrite_head(stack)
        _rewrite_self(stack)





if __name__ == "__main__":
  llist = LinkedList()
  llist.add_to_head(1)
  llist.add_to_head(2)
  llist.add_to_head(3)
  llist.add_to_head(4)

  print(llist.head.value)
  nnode = llist.head.next_node
  print(nnode.value)
  nnode = nnode.next_node
  print(nnode.value)
  nnode = nnode.next_node
  print(nnode.value)

  llist.reverse_list()