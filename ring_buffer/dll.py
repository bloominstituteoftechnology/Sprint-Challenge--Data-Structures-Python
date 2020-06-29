"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    def __str__(self):
        return f'{self.value}'
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    """ Returns the next node """
    def get_next(self):
        return self.next
        print(f'{self.next.value}')

    """ Returns the previous node """
    def get_prev(self):
        return self.prev



"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)
        # increment list length
        self.length  += 1
        # checks if list has head and tail / not empty
        if not self.head and not self.tail:
            # assign head to newly created node 
            self.head = new_node
            # assign tail to newly created node
            self.tail = new_node
        else: # list is not empty
            # points head as new node's next pointer
            new_node.next = self.head
            # points head's previous pointer to new node
            self.head.prev = new_node
            # assigns the head as the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #grabs the value of the node
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)
        # increment list length
        self.length  += 1
        #check if list is empty
        if not self.head and not self.tail:
            # assign head to newly created node 
            self.head = new_node
            # assign tail to newly created node
            self.tail = new_node
        else: # list is not empty
            # points tail as new node's prev pointer
            new_node.prev = self.tail
            # points head's previous pointer to new node
            self.tail.next = new_node
            # assigns the head as the new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        # checks if the node is the head
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #decrements length of list
        self.length -= 1
        # check if only node
        if self.head is self.tail:
            # replace list head and taill with null
            # the node itself will be garbage collected
            self.head = None
            self. tail = None
        # check if node is head
        elif node is self.head:
            # points the head to node next pointer
            self.head = node.next
            node.delete()
        # check if node is tail
        elif node is self.tail:
            # points tail to node prev pointer
            self.tail = node.prev
            node.delete()
        else: 
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        #How to get max
        current = self.head
        max = self.head.value
        #Loop through nodes
        while(current is not None):
            # Compare value in node to max found
            if current.value > max:
                max = current.value
            current = current.next
        # return max found
        return max
    
    def get_all(self):
        # store elements in array
        elements = []
        #set current pointer to head/beginning of list
        current = self.head
        # traverse the list and store elements in arr
        while current is not None:
            elements.append(current.value)
            current = current.get_next()

        return elements
        


        
