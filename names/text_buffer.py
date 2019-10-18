class TextBuffer:
    def __init__(self, init=None):
        self.storage = DoublyLinkedList()
        if init:
            self.append(init)

    def __str__(self):
        s = ""
        current = self.storage.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        #for char in string_to_add:
        for char in string_to_add[::-1]:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_head(_)

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_tail()

    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        other_buffer.storage.head = self.storage.head
        self.storage.tail = other_buffer.storage.tail

    def split(self, split_location):
        pass

    def join_string(self, string_to_join):
        self.append(string_to_join)

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
                node = self.storage[key]
                node.value = (key, value)
                self.order.move_to_end(node)
                return
            if self.size == self.limit:
                node = self.order.head  # Get the oldest node in the cache
                node_value = node.value  # Tuple storing (key, value)
                key_for_dict = node_value[0]  # get key for dict
                del self.storage[key_for_dict]
                self.order.remove_from_head()
                # del self.storage[self.order.remove_from_head()[0]] # Another way to write above 2 lines
                self.size -= 1

            # Adds the given key-value pair to the cache.
            # Add to LL at the tail
            self.order.add_to_tail((key, value))
            # Add to dictionary
            self.storage[key] = self.order.tail
            self.size += 1