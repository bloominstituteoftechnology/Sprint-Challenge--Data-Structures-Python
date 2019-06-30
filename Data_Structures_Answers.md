Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

1. O(1)  if self.current >= self.capacity:
2. O(1)     self.current = 0
3. O(n)  if None in self.storage:
4. O(1)     self.storage.pop()
5. O(1)      self.storage.insert(self.current, item)
6. O(1)   else:
7. O(1)      self.storage.remove(self.storage[self.current])
8. O(1)      self.storage.insert(self.current, item)
9. O(1)   self.current +=1

O(n)

2. What is the space complexity of your ring buffer's `append` function?

3. What is the runtime complexity of your ring buffer's `get` method?

4. What is the space complexity of your ring buffer's `get` method?


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
