from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item): # 
        if not self.current:
            self.current = self.storage.head # current defaults to head
        if self.storage.length == self.capacity: # when at capacity 
            print(self.current.value)
            self.current.value = item # set the current value to the item
            self.current = self.current.next # increment the current value
        else:
            self.storage.add_to_tail(item) # add to the tail

            
    def get(self): # 
        list_buffer_contents = []
        cursor = self.storage.head
        while cursor:
            list_buffer_contents.append(cursor.value)
            cursor = cursor.next
        return list_buffer_contents


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#         self.cursor = 0

#     def append(self, item):
#         # if len(l) == self.capacity:
#         #     l[cursor] = item
#         # else: 
#         #     l.append(item) #the list backwards
#         # return l
#         if len(self.storage) == self.capacity:
#             if self.cursor == self.capacity:
#                 self.cursor = 0
#             self.storage[self.cursor] = item
#             self.cursor += 1
#         else:
#             self.storage.append(item)

#     def get(self):
        
#         return self.storage

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.cursor = 0
        self.capacity = capacity

    def append(self, item):
        # self.storage.pop(0)
        # self.storage.append(item)
        if len(self.storage) == self.capacity:
            if self.cursor == self.capacity:
                self.cursor = 0
            self.storage[self.cursor] = item
            self.cursor += 1
        else:
            self.storage.append(item)


    def get(self):
        l = []
        for i in self.storage:
            if i != None:
                l.append(i)
        return l


buffer = ArrayRingBuffer(5)
# buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
# buffer.append('f')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())


# # # buffer = RingBuffer(5)
buffer.append('e')
# # # # buffer.append('h')

buffer.append('f')

# # # ['f', 'b', 'c', 'd', 'e']

buffer.append('g')
buffer.append('h')
buffer.append('i')
# # ['f', 'g', 'h', 'i', 'e']


# buffer.append('j')
# buffer.append('k')


#should be ['k', 'g', 'h', 'i', 'j']
print(buffer.get())

        