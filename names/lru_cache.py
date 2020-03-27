"""
LRUCache assignment.
"""
from doubly_linked_list import DoublyLinkedList, ListNode




class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache. 
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dictionary = {}
        self.linkedList = DoublyLinkedList()

    def get(self, key, duplicates):
        if key in self.dictionary:   
            # Append to duplicates
            duplicates.append(key)
            
            node = self.dictionary[key]
            self.linkedList.move_to_end(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        self.linkedList.add_to_tail((key, value))
        self.dictionary[key] = self.linkedList.tail
        self.size += 1
