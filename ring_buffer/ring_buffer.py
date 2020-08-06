
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev= None

# class RingBuffer:
#     def __init__(self,capacity):
#         self.current=[]
#         self.capacity=capacity
#         self.head=None

#     def __repr__(self):
#         return f'{self.current}'
    
#     def __str__(self,value):
#         return f'{value}'

#     def get(self):
#         return self.current

    
#     def append(self,value):
#         #empty RB

#         if len(self.current) == 0:
#             newNode=Node(value)
#             self.current.append(newNode.value)
#             #assign self.oldest to value of an integer to later be plugged in as an index when RingBuffer is full
#             self.oldestIndex=self.current.index(newNode.value)
#             return f'self.oldest={self.oldest} self.current={self.current}'

#         # not empty less than full RB
#         if len(self.current) < self.capacity:
#             newNode=Node(value)
#             self.current.append(newNode.value)
#             return 

#         #Full RB
#         if len(self.current) >self.capacity:
#             newNode=Node(value)
#             self.current[int(self.oldestIndex)]=newNode.value
#             self.oldest=self.oldest+1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev= None

class RingBuffer:
    def __init__(self,capacity):
        self.current=[]
        self.capacity=capacity
        self.head=None

    def __repr__(self):
        return f'{self.current}'
    
    def __str__(self,value):
        return f'{value}'

    def get(self):
        return self.current

    
    def append(self,value):
        #empty RB

        if len(self.current) == 0:
            newNode=Node(value)
            self.current.append(newNode.value)
            #assign self.oldest to value of an integer to later be plugged in as an index when RingBuffer is full
            self.oldest=self.current.index(value)
            return f'self.oldest={self.oldest} self.current={self.current}'

        # not empty less than full RB
        if len(self.current) < self.capacity:
            newNode=Node(value)
            self.current.append(newNode.value)
            f'self.oldest={self.oldest} self.current={self.current}'
            return 

        #Full RB
        if len(self.current) == self.capacity:
            #self.oldest is a pointer to the index of first to overwrite. the oldest value. the rotating head
            #when buffer is full self.oldest travels along the ring always one ahead of the last added value
            f'self.oldest={self.oldest} self.current={self.current}'
            del self.current[self.oldest]
            self.current.insert(int(self.oldest),(value))
            self.oldest+=1
            if self.oldest>self.capacity:
                self.oldest-=self.capacity
                self.oldest-=1
            return

            # self.current[self.oldest]=value

#         if len(self.current) ==self.capacity:
#             newNode=Node(value)
#             self.current[int(self.oldestIndex)]=newNode.value
#             self.oldest=self.oldest+1

