import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# runtime: 3.0849990844726562 seconds
# duplicates = [ name for name in names_1 if name in names_2 ]  # Return the list of duplicates in this data structure


# # 12.839998483657837 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# runtime: 3.0630006790161133 seconds
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()


# Create a new Stack
search = Stack()

# for every name in the FIRST array (name_1), add that to stack
for name in names_1:
    search.push(name)

# for each item in the stack, if it is in the SECOND array(name_2) append to duplicates
for item in search.storage:
    if item in names_2:
        duplicates.append(item)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
