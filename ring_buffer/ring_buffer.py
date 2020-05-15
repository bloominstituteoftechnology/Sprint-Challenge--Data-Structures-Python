"""#### Task 1. Implement a Ring Buffer Data Structure

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.head = None
        self.tail = None
        self.next = None

    def get_next(self):
        return self.next

    # def set_next(self, new_value):
    #     self.next = new_value

    def get_value(self):
        return self.value

    def get_head(self):
        return self.head


class LinkedList:

    def __init__(self, value=None):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert_tail(self, value):
        new_node = Node(value)
        # print('we are going to insert a tail with the value of', new_node.value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            # print('head is currently none so we are creating a new head',
            #       self.head.value)
        else:
            # print('there is a head node so we are creating the next value in the list')
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            current_node.next = new_node
            self.length += 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.get_next()


class RingBuffer:
    def __init__(self, capacity, oldest_value=None):
        self.capacity = capacity
        self.storage = LinkedList()
        self.oldest_value = oldest_value

    def append(self, item):
        # are we at capacity ?
        if self.storage.__len__() < self.capacity:
            self.storage.insert_tail(item)
            self.oldest_value = self.storage.head
        # we are at capacity
        # we need to keep track of what the oldest value is (next to be removed)
        # 3 scenarios --> head --> middle --> tail
        else:
            if self.oldest_value == self.storage.head:
                self.storage.head.value = item
                self.oldest_value = self.storage.head.next
            elif self.oldest_value.next is not None:
                self.oldest_value.value = item
                self.oldest_value = self.oldest_value.next
            else:
                self.oldest_value.value = item
                self.oldest_value = self.storage.head

    def get(self):
        current = self.storage.head
        new_list = []
        while current is not None:
            new_list.append(current.value)
            current = current.next
        return new_list


test = RingBuffer(3)

test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(6)
test.storage.print()
