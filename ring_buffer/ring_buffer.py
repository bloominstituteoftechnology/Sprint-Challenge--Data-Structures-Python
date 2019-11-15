from dll_queue import Queue

class RingBuffer:

  def __init__(self, capacity):
    self.capacity = capacity
    
    # comment out these to enable queue mode
    self.current = 0
    self.storage = [None]*capacity
    
    # # comment out these to enable list mode
    # self.storage = Queue()
    # self.current = 0


  # the below implementation uses a fixed length list/array and over
  # writes values based on the index

  def append(self, item):
        
    if self.current >= self.capacity:
      # overright the last element with the first
      self.current += 1
      index = (self.current % self.capacity) -1
      self.storage[index] = item
    
    else:
      # base case
      self.current += 1
      index = (self.current) -1
      self.storage[index] = item

  def get(self):
    if self.current >= self.capacity:
      return self.storage
    else:
      return [x for x in self.storage if x is not None]

  # below is an implementation using a queue
  # def append(self, item):
    
  #   print(f'self.current {self.current}')
  #   print(f'queue len {self.storage.len()}')

  #   if self.current < self.capacity:
  #     print(f'enqueing {item}')
  #     self.storage.enqueue(item)
  #     self.current = self.storage.len()

  #   else:
  #     self.storage.enqueue(item)
  #     self.storage.dequeue()
  #     self.current = self.storage.len()

  # def get(self):
    
  #   val = []
  #   for _ in range(0, self.current):
  #     x = self.storage.dequeue()
  #     print(f'getting {x}')
  #     val.append(x)
  #   return val