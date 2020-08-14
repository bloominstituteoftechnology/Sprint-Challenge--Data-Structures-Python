"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"N: {self.value}"
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"Head: {self.head}\nTail: {self.tail}\nLength: {self.length}"
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create variable to hold the new node 
        # & assign its next to the current list head
        new_node = ListNode(value)
        new_node.next = self.head
        
        # if list is empty, make first added node the tail
        if self.head is None:
            self.tail = new_node
        # if list already has items in it, assign the new node
        # to be the previous of the current head
        else:
            self.head.prev = new_node
        
        # set the head of the list to the new node & increase length
        self.head = new_node
        self.length += 1
        return self

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if there is already no head, do nothing
        if self.head is None:
            return self
        value = self.head.value
        # if the head and tail are the same, 'reset' list
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return value
        # set head to next item in list & reduce length
        else:
            self.head = self.head.next
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create variable to hold the new node 
        # & assign its prev to the current list tail
        new_node = ListNode(value)
        new_node.prev = self.tail
        
        # if list is empty, make first added node the head
        if self.tail is None:
            self.head = new_node
        # if list already has items in it, assign the new node
        # to be the next of the current tail
        else:
            self.tail.next = new_node
        
        # set the tail of the list to the new node & increase length
        self.tail = new_node
        self.length += 1
        return self
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if there is already no tail, do nothing
        if self.tail == None:
            return self
        value = self.tail.value
        # if the tail and head are the same, 'reset' list
        if self.tail is self.head:
            self.tail = None
            self.head = None
            self.length = 0
            return value
        # set tail to prev item in list & reduce length
        else:
            self.tail = self.tail.prev
            self.length -= 1
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if theres nothing in the list or only one item, do nothing
        if self.length == 0 or self.length == 1:
            pass

        # if current node is already the head, do nothing
        if self.head == node:
            pass
        
        elif self.length == 2:
            self.tail = self.head
            self.head.prev = None
            self.length -= 1
            self.add_to_head(node.value)
            return self

        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            self.add_to_head(node.value)
            return self
        else:
            # copy current node
            curr_node = node
            next_node = node.next
            prev_node = node.prev
            # assign prev & next nodes to each other
            prev_node.next = next_node
            next_node.prev = prev_node
            
            # assign current node to head's previous
            self.head.prev = curr_node
            curr_node.next = self.head

            # make current node the new head
            self.head = curr_node
            return self


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if theres nothing in the list or only one item, do nothing
        if self.length == 0 or self.length == 1:
            return self

        # if current node is already the tail, do nothing
        if self.tail == node:
            return self
        
        elif self.length == 2:
            self.head = self.tail
            self.tail.next = None
            self.length -= 1
            self.add_to_tail(node.value)
            return self
        
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            self.add_to_tail(node.value)
        else:
            # copy current node
            curr_node = node
            print(node)
            next_node = node.next
            prev_node = node.prev
            # assign prev & next nodes to each other
            node.prev = prev_node
            node.next = next_node

            # assign current node to tail's next
            self.tail.next = curr_node
            curr_node.prev = self.tail

            # make current node the new tail
            self.tail = curr_node
            return self

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if list is empty, do nothing
        if self.length == 0:
            pass
        # if list is one item, reset list
        elif node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return self

        # if there are 2 items, check if head or tail
        elif self.length == 2:
            if node == self.head:
                self.tail.prev = None
                self.head = self.tail
                self.length = 1
                return self
            
            if node == self.tail:
                self.head.next = None
                self.tail = self.head
                self.length = 1
                return self

        else:
            # if item to delete is the current tail
            if node == self.tail:
                self.tail = node.prev
                node.prev.next = None
                self.length -= 1
                return self
            # if item to delete is the current head
            elif node == self.head:
                self.head = node.next
                node.next.prev = None
                self.length -= 1
                return self
            
            else: 
                next_node = node.next
                prev_node = node.prev
                node.next.prev = prev_node
                node.prev.next = next_node
                self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return 0
        if self.length == 1:
            return self.head.value

        curr_node = self.head
        max_val = 0
        for num in range(self.length):
            if curr_node.value > max_val:
                max_val = curr_node.value
            
            if curr_node.next == None:
                return max_val
            else:
                curr_node = curr_node.next