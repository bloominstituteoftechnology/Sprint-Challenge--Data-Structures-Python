from linked_list import LinkedList
# noqa

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if not self.storage.head:
      return None
    dq_val = self.storage.head.get_value()
    self.storage.remove_head()
    self.size -= 1
    return dq_val
    

  def len(self):
    return self.size
