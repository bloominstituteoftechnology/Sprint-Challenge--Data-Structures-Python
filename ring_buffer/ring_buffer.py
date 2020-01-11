from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # watch out for capacity limit, dunder length is needed to compare
        if self.storage.length == self.capacity:
            # have to remove item at head
            remove_me = self.storage.head
            self.storage.remove_from_head()
            # now add new item to tail
            self.storage.add_to_tail(item)
            if remove_me == self.current:
                self.current = self.storage.tail

        # add to tail link normal ll
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item) 
            self.current = self.storage.head   
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.length == 0:
            return 'empty ring buffer'

        # get starting value from left 
        active_node = self.current
        list_buffer_contents.append(active_node.value)    

        # verify if more items
        if active_node.next:
            next_node = active_node.next
        else:
            next_node = self.storage.head

        #  loop through until back to starting value
        while next_node != active_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head    


        return list_buffer_contents

       


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = []

    def __len__(self):
        return self.length

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(0)
            #  self.storage.insert(0, item)
            self.storage.append(item)
        else:
            self.storage.append(item)    

    def get(self):
        for item in self.storage:
            print(item)




ab = ArrayRingBuffer(2)
ab.append('a')
ab.append('b')

ab.get()
ab.append('c')
ab.get()

# rb = RingBuffer(3)
# print(rb.get())
# rb.append('a')
# # rb.append('b')
# # rb.append('c')
# print(rb.get())

# rb.append('d')
# print(rb.get())

# rb.append('e')
# print(rb.get())

