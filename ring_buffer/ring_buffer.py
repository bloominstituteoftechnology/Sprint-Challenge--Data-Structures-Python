class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LLQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,item):
        temp = Node(item)
        if  self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.front is None:
            return
        temp =self.front
        self.front=temp.next

        if(self.front is None):
            self.rear is None

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = []
        self.__len__ = 0
        self.front =None
        self.rear=None

        pass

    def append(self, item):
        temp=self.front
        self.front=item
        self.front.next=temp
        self.__len__+=1
        if capacity < self.__len__:
            self.last=self.front
        temp= self.lastadded
        self.lastadded=item
        self.lastadded.last=temp


        temp=self.top
        self.top=item
        self.top.next=temp
        self.bottom.next=self.top
        if capacity< self.__len__:
            self.bottom=self.top
        

##add item to front
##lenght = empty
## front = item.



        temp=Node(item)
        if self.__len__ is self.capacity:
            


        if self.__len__ < self.capacity:

    

        # empty
        # self.current+1 =1

        # less than capacity
        # self.current+1 <capacity

        # atcapacity
        # self.current+1 >capacity'

    def get(self):
        if self.__len__ = 0:
            return self.current
        elif self.current is not None:
            return self.current
