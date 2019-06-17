# Hash Map


class HashMap:
    def __init__(self, size, is_value=True):
        self.size = size
        self.map = [None] * self.size
        self.is_value = is_value

    def _get_hash(self, key):
        hash = 0
        m = 2
        for char in str(key):
            hash += ord(char) * m
            m *= 2
        return hash % self.size

    def add(self, key, value=None):
        # b = (key == 'Alvaro Robbins')
        # if b:
        #     print('in b for ', key)
        key_hash = self._get_hash(key)
        if value is None:
            key_value = key
        else:
            key_value = [key, value]

        if self.map[key_hash] is None:
            # if b:
            #     print('creating new list hash', key_hash)
            self.map[key_hash] = list(
                [key_value]) #if not self.is_value else key_value)
            # if b:
            #     print('add map', self.map[key_hash])
            return self
        else:
            if not self.is_value:
                for pair in self.map[key_hash]:
                    if pair[0] == key:
                        pair[1] = value
                        # if b:
                        #     print('match found return True')
                        return True
            else:
                for _value in self.map[key_hash]:
                    if _value == key:
                        return self
            # if b:
            #     print('appending')
            self.map[key_hash].append(key_value)
            return self

    def get(self, key):
        key_hash = self._get_hash(key)
        # b = (key_hash == 612146)
        # if b:
        #     map = self.map[key_hash]
        #     print("in get for ", key, *[map] if len(map) > 1 else map )

        if self.map[key_hash] is not None:
            if self.is_value:
                map = self.map[key_hash]                        
                for value in map:
                    # if b:
                    #     print('test value', value)
                    if value == key:
                        return True
            else:
                for pair in self.map[key_hash]:
                    if pair[0] == key:
                        return pair[1]
        return False

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.is_value:
                if self.map[key_hash][i] == key:
                    self.map[key_hash].pop(i)
                    return True
            else:
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))

# h = HashMap()
# h.add('Bob', '567-8888')
# h.add('Ming', '293-6753')
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.print()
# h.delete('Bob')
# h.print()
# print('Ming: ' + h.get('Ming'))
# print(h.keys())
