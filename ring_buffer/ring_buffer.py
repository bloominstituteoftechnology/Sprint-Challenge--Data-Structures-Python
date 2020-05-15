from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to make sure the size of the storage is less than the
        # pre-determined capacity 
        if len(self.storage) < self.capacity:
            # add to tail to prevent checking for head == None
            # set current_node variable to the head
            self.storage.add_to_tail(item)
            self.current_node = self.storage.head
        else: # the capacity has been reached
            # check if the current node has a next
            if not self.current_node.next:
                # if not, set the current node's value equal to the item
                # and set the current node to be the head
                self.current_node.value = item
                self.current_node = self.storage.head
            else: # the current node has a next link
                # set the current node's value equal to the item
                # and move the current node to the next node to
                # replace that value as it is the next oldest
                self.current_node.value = item
                self.current_node = self.current_node.next

    def get(self):
        # create a blank array
        arr = []
        # create a current variable and set it to the head
        current = self.storage.head
        while current: # while there are still a current value
            # append the value to the array
            arr.append(current.value)
            # move the current reference to the next node
            current = current.next
        return arr
