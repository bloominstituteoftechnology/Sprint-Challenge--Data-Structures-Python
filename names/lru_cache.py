from doubly_linked_list import DoublyLinkedList as DLL

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
        self.num_nodes = 0
        # values in cache_list are key/value dicts
        self.cache_list = DLL()
        # storage holds key, node pairs
        self.storage = {}

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
            self.cache_list.move_to_front(node)
            return node.value[key]

        else:
            return None

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
        # if this is an existing key in the storage cache, 
        # delete the corresponding node in the list
        if key in self.storage:
            self.cache_list.delete(self.storage[key])
            self.num_nodes -= 1
        
        self.cache_list.add_to_head({key: value})
        self.storage[key] = self.cache_list.head
        self.num_nodes += 1
        
        # if cache at max capacity
        if self.num_nodes > self.max_nodes:
            remove_key = list(self.cache_list.tail.value.keys())[0]
            del self.storage[remove_key]
            self.num_nodes -= 1
