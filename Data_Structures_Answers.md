Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?


#  def append(self, item):

#    try:
#        self.storage[self.current] = item -- O(1)
#        self.current += 1 -- O(1)
#
#    except:
#      self.current = 0 -- O(1)
#      self.append(item) -- O(1)

The time complexity seems to simplify to O(1)

2. What is the space complexity of your ring buffer's `append` function?

#  def append(self, item):

#    try:
#        self.storage[self.current] = item -- O(1)
#        self.current += 1 -- O(1)
#
#    except:
#      self.current = 0 -- O(1)
#      self.append(item) -- O(1)

The space complexity seems to simplify to O(1)... this is because at any given function call it is primarily using memory for two items ... the storage variable and the current variable.

3. What is the runtime complexity of your ring buffer's `get` method?


#  def get(self):
#    items = [item for item in self.storage if item != None] -- O(1)
#    return items -- O(1)

The time complexity seems to simplify to O(1) ... Because it includes an assignment, and a return, which both are constant runtime.


4. What is the space complexity of your ring buffer's `get` method?

#  def get(self):
#    items = [item for item in self.storage if item != None] -- O(n)
#    return items -- O(1)

The space complexity seems to simplify to O(n) ... Because memory is required to hold n items, until the list comprehension is complete.

If list comprehensions save each item after comparison, the space complexity could be 0(1)


5. What is the runtime complexity of the provided code in `names.py`?

# for name_1 in names_1: -- O(n)
#     for name_2 in names_2: -- O(n)
#         if name_1 == name_2: -- O(1)
#             duplicates.append(name_1) -- O(1)

The time complexity seems to simplify to O(n^2) ... Because of the double for loop.

6. What is the space complexity of the provided code in `names.py`?

# for name_1 in names_1: -- O(n)
#     for name_2 in names_2: -- O(n)
#         if name_1 == name_2: -- O(1)
#             duplicates.append(name_1) -- O(1)

7. What is the runtime complexity of your optimized code in `names.py`?

# duplicates = list(set(names_1).intersection(names_2)) -- O(1)

The time complexity seems to simplify to O(1) ... Because it is an assignment, it runs in constant time.

8. What is the space complexity of your optimized code in `names.py`?

# duplicates = list(set(names_1).intersection(names_2)) -- O(1)

The space complexity seems to simplify to O(1) ... Because it is comparing two lists at a constant time.
