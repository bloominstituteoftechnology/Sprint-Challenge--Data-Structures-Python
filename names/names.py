import time

start_time = time.time()

with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

class Trie:
    def __init__(self):
        self.children = {}
        self.depth = 0

    def search(self, string):
        c = string[0]

        if c in self.children:
            if len(string) == 1:
                return self.children[c]
            else:
                return self.children[c].search(string[1:])
        else:
            return self

    def insert(self, string):
        if len(string) == 0: return

        c = string[0]

        if c not in self.children:
            self.children[c] = Trie()

        self.children[c].insert(string[1:])

    def insert_many(self, xs):
        for x in xs: self.insert(x)

    def contains_prefix(self, string):
        return self.search(string) is not None

    def contains_exactly(self, string):
        return {} == self.search(string).children 

    def contains_many(self, strings):
        return [self.contains_exactly(string) for string in strings]

trie = Trie()
trie.insert_many(names_1)

duplicates = [name for name in names_2 if trie.contains_exactly(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
