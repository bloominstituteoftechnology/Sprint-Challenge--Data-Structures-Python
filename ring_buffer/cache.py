from doubly_linked_list import *

class Cache:
    
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.dll = DoublyLinkedList()
        self.storage: {str : ListNode} = {}

    @property
    def current_nodes(self):
        return len(self.storage)

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            return node.value

    def set(self, key, value):
        else:
            if self.current_nodes >= self.max_nodes:
                node = self.dll.remove_from_head()
                node_key = None
                for k, v in self.storage.items():
                    if v == node:
                        node_key = k
                if node_key:
                    self.storage.pop(node_key)
            new_node = ListNode(value)
            self.dll.add_to_tail(new_node)
            self.storage[key] = new_node


