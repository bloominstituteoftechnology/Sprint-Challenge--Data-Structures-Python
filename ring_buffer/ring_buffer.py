from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        # self.get_storage = self.storage
        self.counter = 0

    def append(self, item):
        # if self.counter == self.capacity:
        #     self.counter -= self.capacity
            # print(self.capacity)
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            return
            # current = self.storage.head
            # if self.counter > 0:
            #     for i in range(self.counter):
            #         current = current.next
            # current = item
        self.storage.head.value = item
        if self.storage.head.next is not None:
            self.storage.head = self.storage.head.next
        else:
            while self.storage.head.prev is not None:
                self.storage.head = self.storage.head.prev
            # self.counter += 1
            # print(self.counter)
        
        # self.storage.head = self.storage.head
        # self.counter += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # if self.get_storage.head.prev is not None:
        get_storage = self.storage
        while get_storage.head.prev is not None:
            get_storage.head = get_storage.head.prev
            
        if get_storage.head is not None:
            list_buffer_contents += [get_storage.head.value]
            if get_storage.head.next is not None:
                while get_storage.head.next is not None:
                    get_storage.head = get_storage.head.next
                    list_buffer_contents += [get_storage.head.value]
                while get_storage.head.prev is not None:
                    get_storage.head = get_storage.head.prev
        # print(list_buffer_contents)
        self.counter += 1
        print(self.counter)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
