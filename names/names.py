import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


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
    as the new head of the list."""
    def add_to_head(self, value):
        new = ListNode(value)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return
        val = self.head.value
        if self.head is self.tail:
            self.head, self.tail = None, None
            self.length = 0
            return val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        return val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. """
    def add_to_tail(self, value):
        new = ListNode(value)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.tail:
            return
        val = self.tail.value
        if self.tail is self.head:
            self.tail, self.head = None, None
            self.length = 0
            return val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1
        return val

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        val = node.value
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
        node.delete()
        self.length -= 1
        self.add_to_head(val)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        val = node.value
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
        node.delete()
        self.length -= 1
        self.add_to_tail(val)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head is node:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        if self.tail is node:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
        node.delete()
        self.length -= 1
            
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return -1
        max_ = self.head.value
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.value > max_:
                max_ = curr.value
        return max_



class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

    def get(self, key):
        # If key is in storage
        if key in self.storage:
            # move key to end
            node = self.storage[key]
            self.order.move_to_end(node)
            #return value
            return node.value[1]
        # If key is not in storage, return none
        else:
            return None



    def set(self, key, value):

    # If cache is not empty:
        # Check and see if the key is in the dictionary, if dictionary is empty key won't be there
        if key in self.storage:
            # If key is in dict
            node = self.storage[key] # grabbing the full node, if you store whole node in dictionary, you can grab it freely
                # Overwrite the value
            node.value = (key, value)
                # Move it to the end
            self.order.move_to_end(node)
            return

    # If key is not in dict
        # Check and see if cache is full
        if self.size == self.limit: # we get rid of the least recently used one, less likely that it is needed soon, but dictionary - you grab from anywhere
        # If cache is full
            # Remove oldest entry from dictionary and Linked List
            del self.storage[self.order.head.value[0]]
            #delete from linked list
            self.order.remove_from_head()# we arbitrarily decided that the head is the oldest entry
            # Reduce the size
            self.size -= 1

            # If the cache is empty
            # Add to the linked list (key and value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail # references is just a pointer, very low overhead, accessing data with different datatypes is efficient
        # Increment size
        self.size += 1


duplicates = []  # Return the list of duplicates in this data structure

cache = LRUCache(10000)

for x in range(len(names_1)):
    cache.set(names_1[x], names_1[x])


#input a dictionary of one name list, with name1key : name1value
#if i in 2ndlist == name1
for i in names_2:
    if cache.get(i) == i:
    #append
        duplicates.append(i)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
