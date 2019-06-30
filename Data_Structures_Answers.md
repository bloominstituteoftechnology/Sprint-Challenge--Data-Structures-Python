Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

1. O(1)  if self.current >= self.capacity:
2. O(1)     self.current = 0
3. O(1)  self.storage.remove(self.storage[self.current])
4. O(1)  self.storage.insert(self.current, item)
5. O(1)  self.current +=1

O(1)

2. What is the space complexity of your ring buffer's `append` function?

O(1)

3. What is the runtime complexity of your ring buffer's `get` method?

return [item for item in self.storage if item != None]

1. O(n)  for item in self.storage:
2. O(1)     if item != None:
3. O(1)     return item

O(n)

4. What is the space complexity of your ring buffer's `get` method?

O(n)

5. What is the runtime complexity of the provided code in `names.py`?

1. O(1)  duplicates = []
2. O(n)  for name_1 in names_1:
3. O(n)     for name_2 in names_2:
4. O(1)        if name_1 == name_2:
5. O(1)           duplicates.append(name_1)

1 + n (n (1 (1))) =
O(n^2)

6. What is the space complexity of the provided code in `names.py`?

O(n^2)

7. What is the runtime complexity of your optimized code in `names.py`?

1. O(1)  duplicates = []
2. O(1)  name = {}
3. O(n)  for name_1 in names_1:
4. O(1)     names[name_1] = name_1
5. O(n)  for name_2 in names_2:
6. O(1)     if name_2 in names:
7. O(1)         duplicates.append(name_2)

1 + 1 + n(1) + n(1(1)) =
O(2n)

8. What is the space complexity of your optimized code in `names.py`?

O(n)