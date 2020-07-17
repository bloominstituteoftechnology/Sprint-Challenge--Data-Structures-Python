from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = Queue()

    def append(self, item):
        # general case
        if self.queue.__len__() < self.capacity:
            self.queue.enqueue(item)

        # full capacity
        else:
            self.queue.dequeue()
            self.queue.enqueue(item)
        
    def get(self):
        list_ = []
        current = self.queue.storage.head
        list_.append(current.value)
        # itterate through singly-linked list
        while current.get_next():
            current = current.get_next()
            list_.append(current.value)
        return list_


if __name__ == "__main__":
    rb = RingBuffer(3)
    rb.append("a")
    rb.append("b")
    rb.append("c")
    rb.append("d")

    print(rb.get())


