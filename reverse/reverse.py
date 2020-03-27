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
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_value() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def reverse_list(self, a=None, b=None):
        def recursive_reverse(node):
            if node.next_node == None:
                self.head = node
                return
            recursive_reverse(node.next_node)
            temp = node.next_node
            temp.next_node = node
            node.next_node = None
        
        if self.head is not None:
            recursive_reverse(self.head)
        
    #     if self.head is not None:
    #     recursive_reverse(self.head)

    #     # liz
    #     try:
    #         if prev != None:
    #             l2.add_to_head(prev)
    #     except:
    #         l2 = LinkedList()

    #     # base: list is empty
    #     if node == None and prev == None:
    #         try:
    #             return l2
    #         except:
    #             pass

    #     # else: list is not empty
    #     else:
    #         print('else')
    #         prev = node
    #         # print('prev val:', prev.value)
    #         if node:
    #             node = node.get_next()

    #         # print(node.value)
            

    #     return self.reverse_list(node, prev)

l = LinkedList()
l.add_to_head(1)
l.add_to_head(2)
l.add_to_head(3)
l.add_to_head(4)
l.add_to_head(5)
l.reverse_list(l.head, None)
cur = l.head
print(cur.value)
cur = cur.get_next()
print(cur.value)
cur = cur.get_next()
print(cur.value)
cur = cur.get_next()
print(cur.value)
# print(l.reverse_list(l.head, None))