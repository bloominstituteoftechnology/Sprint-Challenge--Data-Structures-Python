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



        