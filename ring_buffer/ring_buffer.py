from doubly_linked_list import DoublyLinkedList

# the RingBuffer can be describe as a linear structure were FIFO operations
# can be performed
# it is a single fixed-size buffer and it is connected end-to-end
class RingBuffer: # initialize the class
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()# were i am saving the list

    def append(self, item):
        # check to see if the length of our storage is not reaching the maximum capacity
        if self.storage.length < self.capacity:
            # if yes add the item in to tail of our doubly linked list
            self.storage.add_to_tail(item)
            # set the current to be equal with the head of our node. This curret will be addressed as the oldest node the first one nod
            self.current = self.storage.head
        else:
            # if the storage reached the maximum volume capacity
            # then pass to current value a new item
            self.current.value = item
            # at this point if the current is equal with the tail of our doubly linked list
            if self.current == self.storage.tail:
                # we are starting again to set the current(olderst node) to be equal with the head storage
                self.current = self.storage.head
            else:
                # otherwise set the oldest one to be equal current next
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []# equal with an empty string
        # we set the node to be equal the head of our storage
        node = self.storage.head
        # at this point we need to loop using while statement
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents