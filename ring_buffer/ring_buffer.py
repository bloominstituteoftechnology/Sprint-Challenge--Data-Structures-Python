# class Node():
#     def __init__(self, data):  # we pass the data we want tthe node to hold
#         self.data = data  # data passed is stored in self.data
#         self.next = None  # pointer, always points to null or None


class Node:
    def __init__(self, value="None", next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None  # beginning of a node, stores a node
        self.tail = None  # aend of a node in the list

    # def __repr__(self):
    #     return str(self.head.value)

    def add_head(self, value):  # append
        new_node = Node(value)
        # if its empty
        # head and tail point to the same node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to current head
            new_node.next_node = self.head
            # moved head to new node
            self.head = new_node

    def add_tail(self, value):
        new_node = Node(value)
        # if its empty
        # head and tail point to the same node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # we have to manipulate the tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:  # if it has one element set head and tail to none
            head_val = self.head.value
            self.head = None
            self.tail = None
            return head_val

        # update head to the right node
        head_val = self.head.value
        self.head = self.head.next_node
        return head_val

    def contains(self, value):
        # see if element exists
        if self.head is None:
            print("Empty")
            return False
        else:
            # loop through eachnode, until we see the value or we cant go further
            current_node = self.head
            while current_node is not None:
                # CHECK if this is the node we are looking for
                if current_node.value == value:
                    return True

                # otherwise, go to the next node
                print(current_node.value, end="->")
                current_node = current_node.next_node
            print("None")
            return False  # we do not have anything in here


# class Circularlinkedlist:
#     def __init__(self):
#         self.head = None

#     def prepend(self, value):
#         # add on to the front of the list
#         new_node = Node(value)
#         current = self.head
#         new_node.next = self.head

#         if not self.head:
#             new_node.next = new_node
#         else:
#             while current.next is not self.head:
#                 current = current.next

#             self.head = new_node

#     def append(self, value):
#         if not self.head:
#             self.head = Node(value)
#             self.head.next = self.head
#         else:
#             new_node = Node(value)
#             current = self.head
#             while current.next is not self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head

#     def print_list(self):
#         print("self.head")
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next
#             if current == self.head:
#                 break


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = []

    def append(self, item):
        print("length in storage right now", len(self.storage))
        print("capacity", self.capacity)
        if len(self.storage) >= self.capacity:
            if self.current >= self.capacity:
                self.current = 0
            self.storage[self.current] = item
            self.current += 1
        else:
            self.storage.append(item)
            self.current += 1
        # self.storage.append(item)
        # self.current += 1

        # print(self.storage)

    def get(self):
        print("self", self.storage)
        return self.storage


if __name__ == '__main__':
    buffer = RingBuffer(3)

    buffer.get()   # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    buffer.get()   # should return ['a', 'b', 'c']

    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    buffer.get()   # should return ['d', 'b', 'c']

    buffer.append('e')
    buffer.append('f')

    buffer.get()   # should return ['d', 'e', 'f']
