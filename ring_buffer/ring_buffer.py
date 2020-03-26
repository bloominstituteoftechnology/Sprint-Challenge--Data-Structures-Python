from doubly_linked_list import DoublyLinkedList
import copy

# fixed cache; when full if new element inserted, oldest element overwritten with newest element (LRU CACHE)
#

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()
        # self.storage = dict()

    def append(self, item):
        if self.current < self.capacity:
            self.storage.add_to_tail(item)

            # print(f'LENGTH = {self.storage.length}')
            self.current += 1
            # print(f'CURRENT = {self.current}')
            # print(f'CAPACITY = {self.capacity}')
            # print(f'ITEM = {item}')
        else:
            # self.storage.length = 5
            # print(self.storage.length)

            # remove LRU from head
            self.storage.remove_from_head()

            # add item to tail
            self.storage.add_to_tail(item)
            self.current += 1
            # print(f'else loop added item = {item}')

            # print(self.storage.length)
            # self.storage.length = self.capacity
            # print(f'FULL{item}')

    def get(self):# returns all elements in the buffer in a list IN GIVEN ORDER;
                  #  NO None VALUES REPORTED EVEN IF EXISTING
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # print(f'outer list {list_buffer_contents}')
        temp_dll = copy.deepcopy(self.storage)
        for i in range(1, self.capacity):
            # print(i)

            # equates item to the head value
            item = temp_dll.head.value

            # print(f'inner loop item = {item}')

            # adds items to the list_buffer_contents
            list_buffer_contents.append(item)

            # removes from head but doesn't replace
            temp_dll.remove_from_head()

            # print(f'inner list {list_buffer_contents}')

        # TODO: Your code here

        return list_buffer_contents

# # ----------------Stretch Goal-------------------
#
#
# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass
#
#     def append(self, item):
#         pass
#
#     def get(self):
#         pass



# from doubly_linked_list import DoublyLinkedList

# fixed cache; when full if new element inserted, oldest element overwritten with newest element (LRU CACHE)
#

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()
#
#     def append(self, item):# add elements to buffer
#         if item in self.storage:
#             element = self.storage[item]
#             element
#         pass
#
#     def get(self):# returns all elements in the buffer in a list IN GIVEN ORDER;
#         #           NO None VALUES REPORTED EVEN IF EXISTING
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []
#
#         # TODO: Your code here
#
#         return list_buffer_contents
