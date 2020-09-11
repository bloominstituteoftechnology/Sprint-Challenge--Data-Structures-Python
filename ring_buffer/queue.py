from singly_linked_list import LinkedList, Node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length()

    def isEmpty(self):
        return self.storage.head == None and self.storage.tail == None

    def enqueue(self, value):
        self.storage.add_to_tail(Node(value))

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            node = self.storage.remove_head()
            return node.get_value()