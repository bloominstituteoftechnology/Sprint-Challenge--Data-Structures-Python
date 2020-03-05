# from doubly_linked_list import DoublyLinkedList
# # A ring buffer is a non-growable buffer with a fixed size. 
# # When the ring buffer is full and a new element is inserted, 
# # the oldest element in the ring buffer is overwritten with 
# # the newest element.


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()

#     # adds elements to the buffer
#     # ou may not use a Python List in your implementation of the append method
#     def append(self, item):
#         capacity_placeholder = self.capacity
#         if capacity_placeholder > 0:
#             self.storage.add_to_tail(item)
#             capacity_placeholder -= 1

#     # returns all of the elements in the buffer 
#     # in a list in their given order. It should 
#     # not return any None values in the list 
#     # even if they are present in the ring buffer.
#     def get(self):
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []
#         list_buffer_contents.append(self.storage.head.value) # add the first to list
        
#         for i in range(1, self.capacity):
#             self.current = self.storage.head.next
#             list_buffer_contents.append(self.current.value) 
#             self.current = self.current.next

#         return list_buffer_contents



# buffer = RingBuffer(4)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')


# # buffer = RingBuffer(5)
# # buffer.append('f')
# print(buffer.get())

# # ----------------Stretch Goal-------------------


# class ArrayRingBuffer: # use a python list
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass








# from doubly_linked_list import DoublyLinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity # limit
#         self.current = None # size
#         self.storage = DoublyLinkedList()
#         # self.size = 0


#     def append(self, item):
#         # adds elements to buffer
#         if self.storage.length == self.capacity:
#             self.storage.remove_from_head()
#             self.storage.add_to_head(item)
#         self.storage.add_to_tail(item)

#         #     self.storage.add_to_tail(item)# item is added to tail
#         #     size -= 1
#         #     print(f'size{size}')
#         # elif self.capacity == 0:
#         #     print(f'size == 0')
#         #     self.storage.remove_from_head()
#         #     self.storage.add_to_tail(item)
#         # if self.capacity == 0:
#         #     self.storage.remove_from_tail()
#             # size += 1
            
#     def get(self): # key
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []
#         # if self.storage.head == None:
#         #     return
#         # # self.current = self.storage.head
#         # # while self.current != None:
#         # #     list_buffer_contents.append(self.current.value)
#         # #     self.current = self.current.next
#         # self.current = self.storage.head
#         # while self.capacity > 0:
#         #     list_buffer_contents.append(self.current.value)
#         #     if not self.current.next:
#         #         break
#         #     self.current = self.current.next
#         #     self.capacity -= 1
#         #     # print(f'capacity {self.capacity}')
#         # # return self.current


#         self.current = self.storage.head
#         while self.capacity > 0:
#         # for i in range(self.capacity):
#             list_buffer_contents.append(self.current.value)
#             if not self.current.next:
#                 self.current = self.current.prev
#             self.current = self.current.next
#             self.capacity -= 1
#         return list_buffer_contents

from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # limit
        self.current = None # size
        self.storage = DoublyLinkedList()
        # self.size = 0


    def append(self, item):
        # adds elements to buffer
        if self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        #     self.storage.add_to_tail(item)# item is added to tail
        #     size -= 1
        #     print(f'size{size}')
        # elif self.capacity == 0:
        #     print(f'size == 0')
        #     self.storage.remove_from_head()
        #     self.storage.add_to_tail(item)
        # if self.capacity == 0:
        #     self.storage.remove_from_tail()
            # size += 1
            
    def get(self): # key
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # if self.storage.head == None:
        #     return
        # # self.current = self.storage.head
        # # while self.current != None:
        # #     list_buffer_contents.append(self.current.value)
        # #     self.current = self.current.next
        # self.current = self.storage.head
        # while self.capacity > 0:
        #     list_buffer_contents.append(self.current.value)
        #     if not self.current.next:
        #         break
        #     self.current = self.current.next
        #     self.capacity -= 1
        #     # print(f'capacity {self.capacity}')
        # # return self.current


        self.current = self.storage.head
        while self.capacity > 0:
        # for i in range(self.capacity):
            list_buffer_contents.append(self.current.value)
            if not self.current.next:
                # self.current = self.current.prev
                return list_buffer_contents
            self.current = self.current.next
            self.capacity -= 1
        return list_buffer_contents


buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
# buffer.append('f')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())


# buffer = RingBuffer(5)
buffer.append('e')
# buffer.append('h')

buffer.append('f')
print(buffer.get())



class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass





    from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item): # when data inserted in buffer, head advances by 1
        # if isfull == False:
        #     # new element cannot be inserted
        # else:
        #     # Buffer[head] = data
        #     item = self.storage.head.value
        #     # increment head pointer
        #     self.storage.next
        #     # if head == tail
        #     if self.storage.head == self.storage.tail:
        #         isfull = True
        if self.current == None:
            self.current = self.storage.head
        if self.storage.length == self.capacity: # if head == tail
            self.storage.head = self.storage.tail# if the ring is full, move the cursor to the head
            self.current.delete()
            self.storage.add_to_tail(item)
            # isfull = True  
            # print('isfull = True  ')
        else:
            # Buffer[head] = data
            self.storage.add_to_tail(item)
            # if self.current.next == None:
             
            # # self.current = self.current.next
            # # increment head pointer
            # # self.storage.next
            # isfull = False
            # # self.current += 1
            # print('isfull = False  ')
            

            
    def get(self): # when data is consumed, tail advances by 1
        list_buffer_contents = []

        # item_in_ll = self.storage.head
        # for i in range(self.capacity):
        #     list_buffer_contents.append(item_in_ll.value)
        #     if item_in_ll.next == None:
        #         print('item_in_ll.next == None')
        #         break
        #     item_in_ll = item_in_ll.next
        cursor = self.storage.head
        while cursor:
            list_buffer_contents.append(cursor.value)
            cursor = cursor.next

        return list_buffer_contents
        # return len(list_buffer_contents)

        #while list is empty
        if not self.current: # set pointer to head first
            self.current = self.storage.head
        # when the capacity is reached, remember it form before
        if self.storage.length == self.capacity:
            # reset the tail to the head of the list

            self.storage.next = self.storage.head
            # insert as usual
            print(f'length==capacity: {self.storage.length}')
        self.storage.add_to_tail(item)
        print(f'length: {self.storage.length}')





buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
# buffer.append('f')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())


# buffer = RingBuffer(5)
buffer.append('e')
# buffer.append('h')

# buffer.append('f')
print(buffer.get())



class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass





    # --------

    # working notes

    from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item): # when data inserted in buffer, head advances by 1
        # self.current = item
        if not self.current:
            self.current = self.storage.head
        if self.storage.length == self.capacity:
            print(self.current.value)
            self.current.value = item
            self.current = self.current.next
            # self.storage.add_to_tail(item)
        else:
            self.storage.add_to_tail(item)
        # self.current = self.storage.head.value
        # self.current = self.storage.head.next

            
    def get(self): # when data is consumed, tail advances by 1
        list_buffer_contents = []
        cursor = self.storage.head
        while cursor:
        # while self.current:
            list_buffer_contents.append(cursor.value)
            # list_buffer_contents.append(self.current.value)
            cursor = cursor.next
            # self.current = self.current.next
        return list_buffer_contents



buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
# buffer.append('f')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())


# # buffer = RingBuffer(5)
buffer.append('e')
# # # buffer.append('h')

buffer.append('f')

# # ['f', 'b', 'c', 'd', 'e']

buffer.append('g')
buffer.append('h')
buffer.append('i')
# # ['f', 'g', 'h', 'i', 'e']


# buffer.append('j')
# buffer.append('k')


#should be ['k', 'g', 'h', 'i', 'j']
print(buffer.get())



class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass