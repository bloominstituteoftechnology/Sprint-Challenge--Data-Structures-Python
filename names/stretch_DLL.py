import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates_2 = []


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # Create instance of ListNode with value
        # increment the DLL length attrubute
        # if DLL is empty
        # if it is empty
        # set head and tail to the new node instance
        # if DLL is not empty
        # set new_nodes next to current head
        # set head's prev to new node
        # set head to new node
        if self.head is None:
            new_node = ListNode(value)
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = ListNode(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # store the value of the head
        # decrement the length of the DLL
        # delete the head
        # if head.next is not None
        # set head.next's prev to None
        # set head to head.next
        # elif head.next is None
        # set head to None
        # set tail to None
        # return the value of the deleted head
        if self.head is None:
            return
        else:
            head_value = self.head.value
            self.delete(self.head)
        return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # Create instance of ListNode with value
        # increment the DLL length attrubute

        # if DLL is empty
        # set head and tail to the new node instance

        # if DLL is not empty
        # set new_nodes prev to current tail
        # set tail's next to new node
        # set tail to new node

        new_node = ListNode(value)
        current_node = self.head
        self.length += 1

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node

        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node
            new_node.next = None

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
        # if tail.prev is not None
        # set tail.prev's next to None
        # set tail to tail.prev
        # elif tail.prev is None
        # set head to None
        # set tail to None
        # return the value of the deleted head

        if self.tail is None:
            return None
        else:
            tail_value = self.tail.value
            self.delete(self.tail)
        return tail_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            current_node_value = node.value
            self.delete(node)
            self.add_to_head(current_node_value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            current_node_value = node.value
            self.delete(node)
            self.add_to_tail(current_node_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # Is the list empty? Then do nothing!

        if self.tail is None and self.head is None:
            return

        # Is the list only one node and is the node passed in
        # the correct node?
        elif self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
            self.length -= 1

        # is the list comprised of multiple nodes?
        # Is the node the head node?
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()

        # Is the node the tail node?
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()

        # Is the node some random node in the list?
        else:
            self.length -= 1
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head is None:
            return None

        current_max = self.head
        current_node = self.head

        while current_node is not None:
            if current_node.next:
                if current_node.value >= current_node.next.value:
                    current_max = current_node
                    current_node = current_node.next
                else:
                    current_max = current_node.next
                    current_node = current_node.next
            else:
                return current_max.value

    def list_contains(self, value):

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

        # current_node = self.head

        # dup_values = []

        # while current_node is not None:
        #     if current_node.value == value:
        #         dup_values.append(value)
        #     current_node = current_node.next
        # return dup_values

    def display_list(self):
        current_node = self.head

        while current_node:
            print(current_node.value)
            current_node = current_node.next


new_names_DLL = DoublyLinkedList()

for name1 in names_1:
    new_names_DLL.add_to_tail(name1)

# new_names_DLL.display_list()


for name2 in names_2:
    if new_names_DLL.list_contains(name2):
        duplicates_2.append(name2)


end_time = time.time()
print(f"{len(duplicates_2)} duplicates:\n\n{', '.join(duplicates_2)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
