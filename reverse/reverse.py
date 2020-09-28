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
        if node is None:
            self.head = prev
            return None
        # print(f"value: {node.value} next.value: {node.get_next().value} ")
        # set the node to prev: node(5) 
        # pass prev node to node.set_next() ie. 4 --> 4-->5
        self.reverse_list(node.get_next(), node)
        node.set_next(prev)
        
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.get_next()

# Testings

list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)
list.add_to_head(6)
list.add_to_head(7)


print("================ List==========================")
list.print_list()
list.reverse_list(list.head, None)
print("================Reverse List==========================")
list.print_list()



# def test_longer_reverse(self):
#     self.list.add_to_head(1)
#     self.list.add_to_head(2)
#     self.list.add_to_head(3)
#     self.list.add_to_head(4)
#     self.list.add_to_head(5)
#     self.assertEqual(self.list.head.value, 5)
#     self.list.reverse_list(self.list.head, None)
#     self.assertEqual(self.list.head.value, 1)
#     self.assertEqual(self.list.head.get_next().value, 2)
#     self.assertEqual(self.list.head.get_next().get_next().value, 3)