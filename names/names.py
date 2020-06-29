import time
import hashlib


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

def answer_1(names_1, names_2):
    # ~ 4x faster
    duplicates = []  # Uses List.  Does not meet criteria.
    for name in names_1:
        if name in names_2:
            duplicates.append(name)
    return duplicates


class HashMap():
    def __init__(self):
        self.storage = {}

    def create_set(self, items):
        i = 0
        for item in items:
            self.storage[item] = i
            i += 1

    def add_items(self, items):
        i = len(self.storage)
        duplicates = []
        for item in items:
            if item in self.storage:
                duplicates.append(item)
            else:
                self.storage[item] = i
                i += 1
        return duplicates


def answer_1b(names_1, names_2):
    map_1 = HashMap()
    map_1.create_set(names_1)
    duplicates = map_1.add_items((names_2))
    return duplicates



### Attempting search tree


class Word():
    def __init__(self, letters:str = None):
        self._build_hash(letters)
        self.letters = letters

    def _build_hash(self, letters):
        self.hash = int(hashlib.sha256(letters.encode('utf-8')).hexdigest(), 16)


class Node():
    def __init__(self, value:Word, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return f'Word: {self.value.letters}'





class SearchTree():
    
    def __init__(self):
        self.head = Node(Word('0'))
        # self.duplicate_attempts = 0
        # self.duplicates = []
    
    
    def add_word(self, word):
        new_word = Word(word)
        terminal = self._check_terminal(new_word)


        if terminal:
            self._add_new_word(new = Node(new_word), branch = terminal)

        elif terminal == False:
            # self.duplicate_attempts += 1
            # self.duplicates.append(word)
            pass

        if terminal is None:
            print(terminal)
            raise ValueError('Terminal None')
    
    def not_exists(self, word):
        return self._check_terminal(Word(word))

    def _check_terminal(self, word):
        return self._lookup(word)
        


    def _lookup(self, word):
        start = self.head
        return self._traverse(start, word)



    def _traverse(self, current_node, word):
        # Check for collision, duplicate
        if current_node.value.hash == word.hash:
            if current_node.value.letters == word.letters:
                return False 
            else:
                return current_node 
        
        # Check Termination
        if self._check_end(current_node):
            return current_node

        # Continue search
        next_node = self._check_direction(current_node, word)

        if next_node is None:
            return current_node
        else:
            return self._traverse(current_node = next_node, word=word)
        

    def _check_end(self, node):
        if node.left is None and node.right is None:
            return True
        return False


    def _check_direction(self, node, value):
        if node.value.hash > value.hash:
            # print(f'Moving Left: {node.value.letters} , {value.letters}')
            return node.left
        elif node.value.hash < value.hash:
            # print(f'Moving Right: {node.value.letters}, {value.letters}')
            return node.right
        return None


    def _add_new_word(self, new: Node, branch: Node):
        
        if new.value.hash < branch.value.hash:
            # print(f'Adding new {new.value.letters} Left Of {branch.value.letters}')
            branch.left = new 
        elif new.value.hash > branch.value.hash: 
            # print(f'Adding new {new.value.letters} Right Of {branch.value.letters}')
            branch.right = new
        else:
            return ValueError('Collision Detected')




def answer_1c(names_1, names_2):
    tree = SearchTree()
    [tree.add_word(word) for word in names_1]
    return [name for name in names_2 if tree.not_exists(name)==False]
        





# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.



# Python has a data structure called Set that can do these comparisons via intersection (time = 0.003s)

def answer_2(names_1, names_2):
    duplicates = set(names_1).intersection(set(names_2))
    return duplicates

def run_test(func, names_1, names_2):
    print('Running: ', func)
    start_time = time.time()
    duplicates = func(names_1, names_2)
    end_time = time.time()
    print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
    print (f"runtime: {end_time - start_time} seconds")

if __name__ == "__main__":
    run_test(answer_1, names_1, names_2)  # Memory constrained list (Stretch in Readme)
    run_test(answer_1b, names_1, names_2)  # Wrapped dictionary Implementation
    run_test(answer_1c, names_1, names_2)  # Binary tree implementation
    run_test(answer_2, names_1, names_2)  # Set implementation
    