from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __str__(self):
        cur_node = self.storage.head
        output = ''
        output += str(cur_node) + ' | '
        if self.storage.head == None and self.storage.tail == None:
            output = "Empty"
        else: 
            while cur_node.next is not None:
                cur_node = cur_node.next
                output += str(cur_node) + ' | '
        return output

    def append(self, item):
        self.storage.add_to_tail(item)

        if self.storage.length > self.capacity: 
            self.storage.remove_from_head()
            self.storage.length += 1
           

           
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur_node = self.storage.head

        while cur_node is not None:
            cur_node = cur_node.next
            list_buffer_contents.append(cur_node)
            

        
        return list_buffer_contents


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass

buffer = RingBuffer(4)



buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')


print(buffer.get())

print(buffer)





