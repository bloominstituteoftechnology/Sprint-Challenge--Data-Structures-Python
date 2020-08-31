from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currrent = None
        self.storage = DoublyLinkedList()

    def append(self, item):
         #if length of storage equals 0
        if len(self.storage) == 0:
            #add item to end
            self.storage.add_to_tail(item)
            #current, None = end
            self.current = self.storage.tail
        #if length of storage is full.
        elif len(self.storage) == self.capacity:
           #if current is equal to end
            if self.current == self.storage.tail:
                #remove tail
                self.storage.remove_from_tail()
                #add to tail
                self.storage.add_to_tail(item)
                #makes current the beginning
                self.current = self.storage.head
                return
            
            oldest = self.current
            #current = current plus 1, (spot next to).
            self.current = self.current.next
            #removes oldest current
            self.storage.delete(oldest)
            #adds item to end
            self.storage.add_to_tail(item)
           #variable = end
            addedNode = self.storage.tail
            
            self.current = self.current.next
           
            while self.current.prev is not addedNode:
                self.storage.move_to_end(self.current.prev)
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)


    def get(self):  
        list_buffer = []
       
        Begin = self.storage.head
        while True:
            list_buffer.append(Begin.value)
            if Begin.next == None:
                #Quit Program
              break
            Begin = Begin.next
            
        print(list_buffer)

        return list_buffer