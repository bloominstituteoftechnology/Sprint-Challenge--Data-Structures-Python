"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

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
        # case where list is empty
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
        
        # normal case
        else:
            self.head.prev = ListNode(value, next=self.head)
            self.head = self.head.prev

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # error handling
        if self.length == 0:
            raise Exception('DoublyLinkedList length = 0. Cannot remove item.')

        val = self.head.value
        self.delete(self.head)
        
        return val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail == None:
            self.tail = ListNode(value)
            self.head = self.tail
        
        else:
            self.tail.next = ListNode(value, prev=self.tail)
            self.tail = self.tail.next

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        val = self.tail.value
        self.delete(self.tail)
        return val

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # case where node is only node
        if node.next == None and node.prev == None:
            self.head = None
            self.tail = None

        # case where node is tail
        elif node.next == None:
            node.prev.next = None
            self.tail = node.prev
        
        # case where node is head
        elif node.prev == None:
            node.next.prev = None
            self.head = node.next

        # case where node is in middle of list
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length == 0:
            raise Exception('No nodes in DoublyLinkedList')

        max = self.head.value
        node = self.head

        for _ in range(self.length-1):
            node = node.next
            if node.value > max:
                max = node.value

        return max
