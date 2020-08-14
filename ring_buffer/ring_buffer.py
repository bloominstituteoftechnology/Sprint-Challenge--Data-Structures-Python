from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        # define how much it can have
        self.capacity = capacity
        #defines which we need to get rid of when a new item is put in
        self.oldest = None
        #going to use my DLT as the base for the structure
        self.storage = DoublyLinkedList()


    def __str__(self):
        return f"Capacity: {self.capacity}\nOldest: {self.oldest}\nListLength: {self.storage.length}"
        

    def append(self, item):
        # if list.length is less than the capacity
        if self.storage.length < self.capacity:
            #  add item to tail
            self.storage.add_to_tail(item)
            # update oldest to current head
            self.oldest = self.storage.head
            print(self.storage.head)
        # if list lenght is at capacity
        elif self.storage.length == self.capacity:
            # find oldest, change value to new item
            self.oldest.value = item
            # if oldest is the tail, set oldest to head
            if self.oldest == self.storage.tail:
                self.oldest = self.storage.head
            # else update oldest to next
            else:
                self.oldest = self.oldest.next

    def get(self):
        # store contents
        list_contents = []
        current = self.storage.head

        while current is not None:
            list_contents.append(current.value)

            current = current.next
        
        return list_contents


# ---- EMULATE TESTS ----- #
# setup
text = "::***********::"
buffer = RingBuffer(5)
print(buffer)

print(text)
# add one element test
buffer.append('a')
print(buffer)

# fill to capacity
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
print(text)
print(buffer)
print(buffer.get())

# add one past buffer
buffer.append('f')
print(text)
print(buffer)
print(buffer.get())

# add many past buffer
buffer.append('g')
buffer.append('h')
buffer.append('i')
print(text)
print(buffer)
print(buffer.get())