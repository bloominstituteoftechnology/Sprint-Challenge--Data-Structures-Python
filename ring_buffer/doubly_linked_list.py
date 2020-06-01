class ListNode:
    def __init__(self, item, prev=None, next=None, counter=0):
        self.item = item
        self.prev = prev
        self.next = next
        self.counter = counter #added



    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0
        self.tally = 0 #added

    def __len__(self):
        return self.length

    def add_to_tail(self, item):
        new_node = ListNode(item)
        self.length += 1
        self.tally += 1
        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail            
        # there is no tail
        else:
            self.head = new_node

        self.tail = new_node
        new_node.counter = self.tally

    def remove_from_head(self):
        item = self.head.item
        self.delete(self.head)

        return item

    # def get_min(self):
    #     return minnode    

    def replace_oldest(self, item): #added
        # find the oldest node
        minvalue = self.head.counter
        checkingnode = self.head
        minnode = self.head

        # found out you can't iterate on self, sooooo...
        while checkingnode is not None:
            if checkingnode.counter < minvalue:
                minvalue = checkingnode.counter

            checkingnode = checkingnode.next
        
        while minnode is not None:
            if minnode.counter == minvalue:
                # minnode is the oldest node
                # we will replace the item and counter of minnode
                self.tally +=1
                # replace minnode with new_node
                minnode.item = item
                minnode.counter = self.tally

            minnode = minnode.next


    def add_to_head(self, item):
        # wrap the given value in a ListNode
        new_node = ListNode(item, None, None)
        self.length += 1
        self.tally += 1
        # handle if list has a head
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        # handle if list has no head
        else:
            self.tail = new_node

        self.head = new_node
        new_node.counter = self.tally


    def remove_from_tail(self):
        # empty list: Not needed but good practice
        if not self.head:
            print("Nothing to see here")
            return None
        
        # List with one node
        elif self.head == self.tail:
            delitem = self.head.item
            self.head = None
            self.tail = None
            self.length -= 1
            return delitem

        # List with more that one node
        else:
            checknode = self.head
            while checknode.next != self.tail:
                checknode = checknode.next
            
            delitem = self.tail.item
            self.tail.delete()
            self.tail = checknode
            self.length -= 1
            return delitem


    def set_tail(self):
        checknode = self.head
        while checknode is not None:
            if checknode.next == None:
                self.tail = checknode

            checknode = checknode.next
            

    def delete(self, node):
        
        # if list is empty
        if not self.head:
            print('I aint got nothing for you bro')
            return
        
        # if list has just one item
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        
        # we have at least two nodes, and the node we want to delete is the head
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.length -= 1

        # we have at least two nodes and the node we want to delete is the tail
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
        
        else:
            node.delete()
            self.length -= 1
  