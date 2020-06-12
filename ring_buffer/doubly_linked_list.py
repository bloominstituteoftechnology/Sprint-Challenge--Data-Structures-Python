class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node: {self.value}"

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        dll_str = f"{self.head}"
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            dll_str = f"{dll_str}\n{current_node}"
        return dll_str

    def remove_from_head(self):
        prev_head = self.head
        if self.length > 1:
            self.head.next.prev = None
            self.head = self.head.next
            prev_head.next = None
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        return prev_head

    def add_to_tail(self, node):
        if self.length < 1:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
            self.length += 1
