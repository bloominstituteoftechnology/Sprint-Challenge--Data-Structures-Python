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


#  # Function to reverse the linked list
#     def reverse(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev

    def reverse_list(self, node, prev):
        prev = None
        node = self.head
        while(node is not None):
            next_node = node.next_node
            node.next_node = prev
            prev = node
            node = next_node
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value),
            temp = temp.next_node


# Print test
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
# llist.reverse_list()
# print("\nReversed Linked List")
# llist.printList()
