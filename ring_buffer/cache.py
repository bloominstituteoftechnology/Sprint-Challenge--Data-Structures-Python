from doubly_linked_list import *

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.dll = DoublyLinkedList()
        self.storage: {str : ListNode} = {}

    @property
    def current_nodes(self):
        return len(self.storage)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.dll.move_to_end(node)
            return node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            node = ListNode(value)
            self.storage[key] = node
            self.dll.move_to_end(node)
            self.dll.tail.value = value
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


