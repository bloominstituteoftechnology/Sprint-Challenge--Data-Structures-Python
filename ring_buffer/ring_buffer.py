from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 #set to zero to start
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Adding the first elements until capacity is reached
        if self.current < self.capacity: 
            self.storage.add_to_tail(item)
            self.current += 1
        # conditional by adding the first element after capacity is reached, or when current is reset again
        elif self.current == self.capacity:
            self.storage.delete(self.storage.head) # removes front of DLL
            self.storage.add_to_head(item) # Add  new item to front of DLL
            self.current += 1
        # this is a case to allow catching when current is over capacity
        else:
            current = self.storage.head # grabs the head
            for i in range(self.current - self.capacity): # Loops thru the amount of times that we need to swap over (i.e. 6 append on 5 capacity, 6-5=1 so we shift over 1)
                if current.next is not None: # is not None grabs the end of loop
                    current = current.next # grabs the next node
            current.insert_before(item) # Once found we insert the item before the node we tracked
            current.delete() # removes node that was replaced with a specific item
            self.current += 1 #increases
            if self.current == (self.capacity * 2): # Once current goes thru the list and ends up replacing all, next reset to act like it is a fresh/new list
                self.current = self.capacity # Set it up to capacity so it hits the second if statement above, and we are fresh

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # It begins at front of the storage
        current = self.storage.head
        # Loops until  hits the end
        while current is not None:
            list_buffer_contents.append(current.value) # Add to return array
            current = current.next # Go to next item
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
