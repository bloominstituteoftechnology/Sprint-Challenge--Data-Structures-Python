from DLL import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Will see is the size of storage is less than expected

        if len(self.storage) < self.capacity: 
            #set current_node to storage head
            #add to tail to prevent checking for head
            self.storage.add_to_tail
            self.current_node = self.storage.head
        else: #Just in case capacity is reached
            #Does the current node have a next?
            if not self.current_node.next:
                self.current_node.value = item
                self.current_node = self.storage.head
            else: 

                self.current_node.value = item
                self.current_node = self.current_node.next
            
        

    def get(self):
        # Make an empty array
        arr = []
        #Create a current variable and set it to head
        current = self.storage.head
        while current: #While there is still a current value, we append to the array
            arr.append(current.value)
            
            current = current.next
        return arr
            

    