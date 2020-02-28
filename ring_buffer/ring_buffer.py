from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

        #!Tests also tell you what you need and !spec in readme

    def append(self, item):
        if self.current == None: #starts at none 
            self.current = self.storage.head #beginning node in dict
        if self.current:
            print(self.current.value, item) #item from append parameter
        if self.capacity == len(self.storage) and self.current == self.storage.head:

            self.storage.remove_from_head() #head
            self.storage.add_to_head(item)

            self.current = self.current.next

        elif self.capacity == len(self.storage) and self.current == self.storage.tail:

            self.storage.remove_from_tail() #tail so list is completed
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.capacity == len(self.storage):
            self.current.insert_after(item) #appending
            self.storage.length += 1  #increment
            temp = self.current.next.next
            self.storage.delete(self.current)

            self.current = temp

        else:
            print("Strike", item, len(self.storage))
            self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = self.storage.head #set temporary list

        list_buffer_contents.append(temp.value)

        while temp != self.storage.tail:
            temp = temp.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
